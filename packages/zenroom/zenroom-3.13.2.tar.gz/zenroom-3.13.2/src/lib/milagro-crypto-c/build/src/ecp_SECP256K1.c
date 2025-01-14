/*
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
*/

/* AMCL Elliptic Curve Functions */
/* SU=m, SU is Stack Usage (Weierstrass Curves) */

//#define HAS_MAIN

#include "ecp_SECP256K1.h"

/* test for P=O point-at-infinity */
int ECP_SECP256K1_isinf(ECP_SECP256K1 *P)
{

#if CURVETYPE_SECP256K1==EDWARDS
    return (FP_SECP256K1_iszilch(&(P->x)) && FP_SECP256K1_equals(&(P->y),&(P->z)));
#endif
#if CURVETYPE_SECP256K1==WEIERSTRASS
    return (FP_SECP256K1_iszilch(&(P->x)) && FP_SECP256K1_iszilch(&(P->z)));
#endif
#if CURVETYPE_SECP256K1==MONTGOMERY
    return FP_SECP256K1_iszilch(&(P->z));
#endif

}

/* Conditional swap of P and Q dependant on d */
static void ECP_SECP256K1_cswap(ECP_SECP256K1 *P,ECP_SECP256K1 *Q,int d)
{
    FP_SECP256K1_cswap(&(P->x),&(Q->x),d);
#if CURVETYPE_SECP256K1!=MONTGOMERY
    FP_SECP256K1_cswap(&(P->y),&(Q->y),d);
#endif
    FP_SECP256K1_cswap(&(P->z),&(Q->z),d);
}

#if CURVETYPE_SECP256K1!=MONTGOMERY
/* Conditional move Q to P dependant on d */
static void ECP_SECP256K1_cmove(ECP_SECP256K1 *P,ECP_SECP256K1 *Q,int d)
{
    FP_SECP256K1_cmove(&(P->x),&(Q->x),d);
#if CURVETYPE_SECP256K1!=MONTGOMERY
    FP_SECP256K1_cmove(&(P->y),&(Q->y),d);
#endif
    FP_SECP256K1_cmove(&(P->z),&(Q->z),d);
}

/* return 1 if b==c, no branching */
static int teq(sign32 b,sign32 c)
{
    sign32 x=b^c;
    x-=1;  // if x=0, x now -1
    return (int)((x>>31)&1);
}
#endif // CURVETYPE_SECP256K1!=MONTGOMERY

#if CURVETYPE_SECP256K1!=MONTGOMERY
/* Constant time select from pre-computed table */
static void ECP_SECP256K1_select(ECP_SECP256K1 *P,ECP_SECP256K1 W[],sign32 b)
{
    ECP_SECP256K1 MP;
    sign32 m=b>>31;
    sign32 babs=(b^m)-m;

    babs=(babs-1)/2;

    ECP_SECP256K1_cmove(P,&W[0],teq(babs,0));  // conditional move
    ECP_SECP256K1_cmove(P,&W[1],teq(babs,1));
    ECP_SECP256K1_cmove(P,&W[2],teq(babs,2));
    ECP_SECP256K1_cmove(P,&W[3],teq(babs,3));
    ECP_SECP256K1_cmove(P,&W[4],teq(babs,4));
    ECP_SECP256K1_cmove(P,&W[5],teq(babs,5));
    ECP_SECP256K1_cmove(P,&W[6],teq(babs,6));
    ECP_SECP256K1_cmove(P,&W[7],teq(babs,7));

    ECP_SECP256K1_copy(&MP,P);
    ECP_SECP256K1_neg(&MP);  // minus P
    ECP_SECP256K1_cmove(P,&MP,(int)(m&1));
}
#endif

/* Test P == Q */
/* SU=168 */
int ECP_SECP256K1_equals(ECP_SECP256K1 *P,ECP_SECP256K1 *Q)
{
    FP_SECP256K1 a,b;

    FP_SECP256K1_mul(&a,&(P->x),&(Q->z));
    FP_SECP256K1_mul(&b,&(Q->x),&(P->z));
    if (!FP_SECP256K1_equals(&a,&b)) return 0;

#if CURVETYPE_SECP256K1!=MONTGOMERY
    FP_SECP256K1_mul(&a,&(P->y),&(Q->z));
    FP_SECP256K1_mul(&b,&(Q->y),&(P->z));
    if (!FP_SECP256K1_equals(&a,&b)) return 0;
#endif

    return 1;

}

/* Set P=Q */
/* SU=16 */
void ECP_SECP256K1_copy(ECP_SECP256K1 *P,ECP_SECP256K1 *Q)
{
    FP_SECP256K1_copy(&(P->x),&(Q->x));
#if CURVETYPE_SECP256K1!=MONTGOMERY
    FP_SECP256K1_copy(&(P->y),&(Q->y));
#endif
    FP_SECP256K1_copy(&(P->z),&(Q->z));
}

/* Set P=-Q */
#if CURVETYPE_SECP256K1!=MONTGOMERY
/* SU=8 */
void ECP_SECP256K1_neg(ECP_SECP256K1 *P)
{
#if CURVETYPE_SECP256K1==WEIERSTRASS
    FP_SECP256K1_neg(&(P->y),&(P->y));
    FP_SECP256K1_norm(&(P->y));
#else
    FP_SECP256K1_neg(&(P->x),&(P->x));
    FP_SECP256K1_norm(&(P->x));
#endif

}
#endif

/* Set P=O */
void ECP_SECP256K1_inf(ECP_SECP256K1 *P)
{
    FP_SECP256K1_zero(&(P->x));
#if CURVETYPE_SECP256K1!=MONTGOMERY
    FP_SECP256K1_one(&(P->y));
#endif
#if CURVETYPE_SECP256K1!=EDWARDS
    FP_SECP256K1_zero(&(P->z));
#else
    FP_SECP256K1_one(&(P->z));
#endif
}

/* Calculate right Hand Side of curve equation y^2=RHS */
/* SU=56 */
void ECP_SECP256K1_rhs(FP_SECP256K1 *v,FP_SECP256K1 *x)
{
#if CURVETYPE_SECP256K1==WEIERSTRASS
    /* x^3+Ax+B */
    FP_SECP256K1 t;
    FP_SECP256K1_sqr(&t,x);
    FP_SECP256K1_mul(&t,&t,x);

    if (CURVE_A_SECP256K1==-3)
    {
        FP_SECP256K1_neg(v,x);
        FP_SECP256K1_norm(v);
        FP_SECP256K1_imul(v,v,-CURVE_A_SECP256K1);
        FP_SECP256K1_norm(v);
        FP_SECP256K1_add(v,&t,v);
    }
    else FP_SECP256K1_copy(v,&t);

    FP_SECP256K1_rcopy(&t,CURVE_B_SECP256K1);

    FP_SECP256K1_add(v,&t,v);
    FP_SECP256K1_reduce(v);
#endif

#if CURVETYPE_SECP256K1==EDWARDS
    /* (Ax^2-1)/(Bx^2-1) */
    FP_SECP256K1 t,one;
    FP_SECP256K1_sqr(v,x);
    FP_SECP256K1_one(&one);
    FP_SECP256K1_rcopy(&t,CURVE_B_SECP256K1);

    FP_SECP256K1_mul(&t,v,&t);
    FP_SECP256K1_sub(&t,&t,&one);
    FP_SECP256K1_norm(&t);
    if (CURVE_A_SECP256K1==1) FP_SECP256K1_sub(v,v,&one);

    if (CURVE_A_SECP256K1==-1)
    {
        FP_SECP256K1_add(v,v,&one);
        FP_SECP256K1_norm(v);
        FP_SECP256K1_neg(v,v);
    }
    FP_SECP256K1_norm(v);
    FP_SECP256K1_inv(&t,&t);
    FP_SECP256K1_mul(v,v,&t);
    FP_SECP256K1_reduce(v);
#endif

#if CURVETYPE_SECP256K1==MONTGOMERY
    /* x^3+Ax^2+x */
    FP_SECP256K1 x2,x3;
    FP_SECP256K1_sqr(&x2,x);
    FP_SECP256K1_mul(&x3,&x2,x);
    FP_SECP256K1_copy(v,x);
    FP_SECP256K1_imul(&x2,&x2,CURVE_A_SECP256K1);
    FP_SECP256K1_add(v,v,&x2);
    FP_SECP256K1_add(v,v,&x3);
    FP_SECP256K1_reduce(v);
#endif
}

#if CURVETYPE_SECP256K1==MONTGOMERY

/* Set P=(x,{y}) */

int ECP_SECP256K1_set(ECP_SECP256K1 *P,BIG_256_28 x)
{
    BIG_256_28 m,b;
    FP_SECP256K1 rhs;
    BIG_256_28_rcopy(m,Modulus_SECP256K1);

    FP_SECP256K1_nres(&rhs,x);

    ECP_SECP256K1_rhs(&rhs,&rhs);
    FP_SECP256K1_redc(b,&rhs);

    if (BIG_256_28_jacobi(b,m)!=1)
    {
        ECP_SECP256K1_inf(P);
        return 0;
    }

    FP_SECP256K1_nres(&(P->x),x);
    FP_SECP256K1_one(&(P->z));
    return 1;
}

/* Extract x coordinate as BIG */
int ECP_SECP256K1_get(BIG_256_28 x,ECP_SECP256K1 *P)
{
    ECP_SECP256K1 W;
    ECP_SECP256K1_copy(&W,P);
    ECP_SECP256K1_affine(&W);
    if (ECP_SECP256K1_isinf(&W)) return -1;
    FP_SECP256K1_redc(x,&(W.x));
    return 0;
}


#else
/* Extract (x,y) and return sign of y. If x and y are the same return only x */
/* SU=16 */
int ECP_SECP256K1_get(BIG_256_28 x,BIG_256_28 y,ECP_SECP256K1 *P)
{
    ECP_SECP256K1 W;
    int s;
    ECP_SECP256K1_copy(&W,P);
    ECP_SECP256K1_affine(&W);

    if (ECP_SECP256K1_isinf(&W)) return -1;

    FP_SECP256K1_redc(y,&(W.y));
    s=BIG_256_28_parity(y);

    FP_SECP256K1_redc(x,&(W.x));

    return s;
}

/* Set P=(x,{y}) */
/* SU=96 */
int ECP_SECP256K1_set(ECP_SECP256K1 *P,BIG_256_28 x,BIG_256_28 y)
{
    FP_SECP256K1 rhs,y2;

    FP_SECP256K1_nres(&y2,y);
    FP_SECP256K1_sqr(&y2,&y2);
    FP_SECP256K1_reduce(&y2);

    FP_SECP256K1_nres(&rhs,x);
    ECP_SECP256K1_rhs(&rhs,&rhs);

    if (!FP_SECP256K1_equals(&y2,&rhs))
    {
        ECP_SECP256K1_inf(P);
        return 0;
    }

    FP_SECP256K1_nres(&(P->x),x);
    FP_SECP256K1_nres(&(P->y),y);
    FP_SECP256K1_one(&(P->z));
    return 1;
}

/* Set P=(x,y), where y is calculated from x with sign s */
/* SU=136 */
int ECP_SECP256K1_setx(ECP_SECP256K1 *P,BIG_256_28 x,int s)
{
    FP_SECP256K1 rhs;
    BIG_256_28 t,m;
    BIG_256_28_rcopy(m,Modulus_SECP256K1);

    FP_SECP256K1_nres(&rhs,x);

    ECP_SECP256K1_rhs(&rhs,&rhs);

    FP_SECP256K1_redc(t,&rhs);
    if (BIG_256_28_jacobi(t,m)!=1)
    {
        ECP_SECP256K1_inf(P);
        return 0;
    }

    FP_SECP256K1_nres(&(P->x),x);
    FP_SECP256K1_sqrt(&(P->y),&rhs);

    FP_SECP256K1_redc(t,&(P->y));

    if (BIG_256_28_parity(t)!=s)
        FP_SECP256K1_neg(&(P->y),&(P->y));
    FP_SECP256K1_reduce(&(P->y));
    FP_SECP256K1_one(&(P->z));
    return 1;
}

#endif

void ECP_SECP256K1_cfp(ECP_SECP256K1 *P)
{
    /* multiply point by curves cofactor */
    BIG_256_28 c;
    int cf=CURVE_Cof_I_SECP256K1;
    if (cf==1) return;
    if (cf==4)
    {
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        return;
    }
    if (cf==8)
    {
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        return;
    }
    BIG_256_28_rcopy(c,CURVE_Cof_SECP256K1);
    ECP_SECP256K1_mul(P,c);
    return;
}

/* map BIG to point on curve of correct order */
/* The BIG should be the output of some hash function */

void ECP_SECP256K1_mapit(ECP_SECP256K1 *P,octet *W)
{
    BIG_256_28 q,x;
    BIG_256_28_fromBytes(x,W->val);
    BIG_256_28_rcopy(q,Modulus_SECP256K1);
    BIG_256_28_mod(x,q);

    for (;;)
    {
        for (;;)
        {
#if CURVETYPE_SECP256K1!=MONTGOMERY
            ECP_SECP256K1_setx(P,x,0);
#else
            ECP_SECP256K1_set(P,x);
#endif
            BIG_256_28_inc(x,1);
            BIG_256_28_norm(x);
            if (!ECP_SECP256K1_isinf(P)) break;
        }
        ECP_SECP256K1_cfp(P);
        if (!ECP_SECP256K1_isinf(P)) break;
    }
}

/* Convert P to Affine, from (x,y,z) to (x,y) */
/* SU=160 */
void ECP_SECP256K1_affine(ECP_SECP256K1 *P)
{
    FP_SECP256K1 one,iz;
    if (ECP_SECP256K1_isinf(P)) return;
    FP_SECP256K1_one(&one);
    if (FP_SECP256K1_equals(&(P->z),&one)) return;

    FP_SECP256K1_inv(&iz,&(P->z));
    FP_SECP256K1_mul(&(P->x),&(P->x),&iz);

#if CURVETYPE_SECP256K1==EDWARDS || CURVETYPE_SECP256K1==WEIERSTRASS

    FP_SECP256K1_mul(&(P->y),&(P->y),&iz);
    FP_SECP256K1_reduce(&(P->y));

#endif

    FP_SECP256K1_reduce(&(P->x));
    FP_SECP256K1_copy(&(P->z),&one);
}

/* SU=120 */
void ECP_SECP256K1_outputxyz(ECP_SECP256K1 *P)
{
    BIG_256_28 x,z;
    if (ECP_SECP256K1_isinf(P))
    {
        printf("Infinity\n");
        return;
    }
    FP_SECP256K1_reduce(&(P->x));
    FP_SECP256K1_redc(x,&(P->x));
    FP_SECP256K1_reduce(&(P->z));
    FP_SECP256K1_redc(z,&(P->z));

#if CURVETYPE_SECP256K1!=MONTGOMERY
    BIG_256_28 y;
    FP_SECP256K1_reduce(&(P->y));
    FP_SECP256K1_redc(y,&(P->y));
    printf("(");
    BIG_256_28_output(x);
    printf(",");
    BIG_256_28_output(y);
    printf(",");
    BIG_256_28_output(z);
    printf(")\n");

#else
    printf("(");
    BIG_256_28_output(x);
    printf(",");
    BIG_256_28_output(z);
    printf(")\n");
#endif
}

/* SU=16 */
/* Output point P */
void ECP_SECP256K1_output(ECP_SECP256K1 *P)
{
    BIG_256_28 x;
    if (ECP_SECP256K1_isinf(P))
    {
        printf("Infinity\n");
        return;
    }
    ECP_SECP256K1_affine(P);
#if CURVETYPE_SECP256K1!=MONTGOMERY
    BIG_256_28 y;
    FP_SECP256K1_redc(x,&(P->x));
    FP_SECP256K1_redc(y,&(P->y));
    printf("(");
    BIG_256_28_output(x);
    printf(",");
    BIG_256_28_output(y);
    printf(")\n");
#else
    FP_SECP256K1_redc(x,&(P->x));
    printf("(");
    BIG_256_28_output(x);
    printf(")\n");
#endif
}

/* SU=16 */
/* Output point P */
void ECP_SECP256K1_rawoutput(ECP_SECP256K1 *P)
{
    BIG_256_28 x,z;

#if CURVETYPE_SECP256K1!=MONTGOMERY
    BIG_256_28 y;
    FP_SECP256K1_redc(x,&(P->x));
    FP_SECP256K1_redc(y,&(P->y));
    FP_SECP256K1_redc(z,&(P->z));
    printf("(");
    BIG_256_28_output(x);
    printf(",");
    BIG_256_28_output(y);
    printf(",");
    BIG_256_28_output(z);
    printf(")\n");
#else
    FP_SECP256K1_redc(x,&(P->x));
    FP_SECP256K1_redc(z,&(P->z));
    printf("(");
    BIG_256_28_output(x);
    printf(",");
    BIG_256_28_output(z);
    printf(")\n");
#endif
}

/* SU=88 */
/* Convert P to octet string */
void ECP_SECP256K1_toOctet(octet *W,ECP_SECP256K1 *P,bool compress)
{
#if CURVETYPE_SECP256K1==MONTGOMERY
    BIG_256_28 x;
    ECP_SECP256K1_get(x,P);
    W->len=MODBYTES_256_28+1;
    W->val[0]=6;
    BIG_256_28_toBytes(&(W->val[1]),x);
#else
    BIG_256_28 x,y;
    ECP_SECP256K1_get(x,y,P);
    if (compress)
    {
        W->val[0]=0x02;
        if (BIG_256_28_parity(y)==1) W->val[0]=0x03;
        W->len=MODBYTES_256_28+1;
        BIG_256_28_toBytes(&(W->val[1]),x);
    }
    else
    {
        W->val[0]=4;
        W->len=2*MODBYTES_256_28+1;
        BIG_256_28_toBytes(&(W->val[1]),x);
        BIG_256_28_toBytes(&(W->val[MODBYTES_256_28+1]),y);
    }
#endif
}

/* SU=88 */
/* Restore P from octet string */
int ECP_SECP256K1_fromOctet(ECP_SECP256K1 *P,octet *W)
{
#if CURVETYPE_SECP256K1==MONTGOMERY
    BIG_256_28 x;
    BIG_256_28_fromBytes(x,&(W->val[1]));
    if (ECP_SECP256K1_set(P,x)) return 1;
    return 0;
#else
    BIG_256_28 x,y;
    int typ=W->val[0];
    BIG_256_28_fromBytes(x,&(W->val[1]));
    if (typ==0x04)
    {
        BIG_256_28_fromBytes(y,&(W->val[MODBYTES_256_28+1]));
        if (ECP_SECP256K1_set(P,x,y)) return 1;
    }
    if (typ==0x02 || typ==0x03)
    {
        if (ECP_SECP256K1_setx(P,x,typ&1)) return 1;
    }
    return 0;
#endif
}


/* Set P=2P */
/* SU=272 */
void ECP_SECP256K1_dbl(ECP_SECP256K1 *P)
{
#if CURVETYPE_SECP256K1==WEIERSTRASS
    FP_SECP256K1 t0,t1,t2,t3,x3,y3,z3,b;

    if (CURVE_A_SECP256K1==0)
    {
        FP_SECP256K1_sqr(&t0,&(P->y));					//t0.sqr();
        FP_SECP256K1_mul(&t1,&(P->y),&(P->z));			//t1.mul(z);

        FP_SECP256K1_sqr(&t2,&(P->z));					//t2.sqr();
        FP_SECP256K1_add(&(P->z),&t0,&t0);		//z.add(t0);
        FP_SECP256K1_norm(&(P->z));					//z.norm();
        FP_SECP256K1_add(&(P->z),&(P->z),&(P->z));	//z.add(z);
        FP_SECP256K1_add(&(P->z),&(P->z),&(P->z));	//z.add(z);
        FP_SECP256K1_norm(&(P->z));					//z.norm();

        FP_SECP256K1_imul(&t2,&t2,3*CURVE_B_I_SECP256K1);		//t2.imul(3*ROM.CURVE_B_I);
        FP_SECP256K1_mul(&x3,&t2,&(P->z));			//x3.mul(z);

        FP_SECP256K1_add(&y3,&t0,&t2);				//y3.add(t2);
        FP_SECP256K1_norm(&y3);						//y3.norm();
        FP_SECP256K1_mul(&(P->z),&(P->z),&t1);		//z.mul(t1);

        FP_SECP256K1_add(&t1,&t2,&t2);				//t1.add(t2);
        FP_SECP256K1_add(&t2,&t2,&t1);				//t2.add(t1);
        FP_SECP256K1_sub(&t0,&t0,&t2);				//t0.sub(t2);
        FP_SECP256K1_norm(&t0);						//t0.norm();
        FP_SECP256K1_mul(&y3,&y3,&t0);				//y3.mul(t0);
        FP_SECP256K1_add(&y3,&y3,&x3);				//y3.add(x3);
        FP_SECP256K1_mul(&t1,&(P->x),&(P->y));			//t1.mul(y);

        FP_SECP256K1_norm(&t0);					//x.norm();
        FP_SECP256K1_mul(&(P->x),&t0,&t1);		//x.mul(t1);
        FP_SECP256K1_add(&(P->x),&(P->x),&(P->x));	//x.add(x);
        FP_SECP256K1_norm(&(P->x));					//x.norm();
        FP_SECP256K1_copy(&(P->y),&y3);				//y.copy(y3);
        FP_SECP256K1_norm(&(P->y));					//y.norm();
    }
    else // its -3
    {

        if (CURVE_B_I_SECP256K1==0)					//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_rcopy(&b,CURVE_B_SECP256K1);		//b.copy(new FP(new BIG(ROM.CURVE_B)));

        FP_SECP256K1_sqr(&t0,&(P->x));					//t0.sqr();  //1    x^2
        FP_SECP256K1_sqr(&t1,&(P->y));					//t1.sqr();  //2    y^2
        FP_SECP256K1_sqr(&t2,&(P->z));					//t2.sqr();  //3

        FP_SECP256K1_mul(&t3,&(P->x),&(P->y));			//t3.mul(y); //4
        FP_SECP256K1_add(&t3,&t3,&t3);				//t3.add(t3);
        FP_SECP256K1_norm(&t3);						//t3.norm();//5

        FP_SECP256K1_mul(&z3,&(P->z),&(P->x));			//z3.mul(x);   //6
        FP_SECP256K1_add(&z3,&z3,&z3);				//z3.add(z3);
        FP_SECP256K1_norm(&z3);						//z3.norm();//7

        if (CURVE_B_I_SECP256K1==0)						//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_mul(&y3,&t2,&b);				//y3.mul(b); //8
        else
            FP_SECP256K1_imul(&y3,&t2,CURVE_B_I_SECP256K1);	//y3.imul(ROM.CURVE_B_I);

        FP_SECP256K1_sub(&y3,&y3,&z3);				//y3.sub(z3); //y3.norm(); //9  ***
        FP_SECP256K1_add(&x3,&y3,&y3);				//x3.add(y3);
        FP_SECP256K1_norm(&x3);						//x3.norm();//10

        FP_SECP256K1_add(&y3,&y3,&x3);				//y3.add(x3); //y3.norm();//11
        FP_SECP256K1_sub(&x3,&t1,&y3);				//x3.sub(y3);
        FP_SECP256K1_norm(&x3);						//x3.norm();//12
        FP_SECP256K1_add(&y3,&y3,&t1);				//y3.add(t1);
        FP_SECP256K1_norm(&y3);						//y3.norm();//13
        FP_SECP256K1_mul(&y3,&y3,&x3);				//y3.mul(x3); //14
        FP_SECP256K1_mul(&x3,&x3,&t3);				//x3.mul(t3); //15
        FP_SECP256K1_add(&t3,&t2,&t2);				//t3.add(t2);  //16
        FP_SECP256K1_add(&t2,&t2,&t3);				//t2.add(t3); //17

        if (CURVE_B_I_SECP256K1==0)					//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_mul(&z3,&z3,&b);				//z3.mul(b); //18
        else
            FP_SECP256K1_imul(&z3,&z3,CURVE_B_I_SECP256K1);	//z3.imul(ROM.CURVE_B_I);

        FP_SECP256K1_sub(&z3,&z3,&t2);				//z3.sub(t2); //z3.norm();//19
        FP_SECP256K1_sub(&z3,&z3,&t0);				//z3.sub(t0);
        FP_SECP256K1_norm(&z3);						//z3.norm();//20  ***
        FP_SECP256K1_add(&t3,&z3,&z3);				//t3.add(z3); //t3.norm();//21

        FP_SECP256K1_add(&z3,&z3,&t3);				//z3.add(t3);
        FP_SECP256K1_norm(&z3);						//z3.norm(); //22
        FP_SECP256K1_add(&t3,&t0,&t0);				//t3.add(t0); //t3.norm(); //23
        FP_SECP256K1_add(&t0,&t0,&t3);				//t0.add(t3); //t0.norm();//24
        FP_SECP256K1_sub(&t0,&t0,&t2);				//t0.sub(t2);
        FP_SECP256K1_norm(&t0);						//t0.norm();//25

        FP_SECP256K1_mul(&t0,&t0,&z3);				//t0.mul(z3);//26
        FP_SECP256K1_add(&y3,&y3,&t0);				//y3.add(t0); //y3.norm();//27
        FP_SECP256K1_mul(&t0,&(P->y),&(P->z));			//t0.mul(z);//28
        FP_SECP256K1_add(&t0,&t0,&t0);				//t0.add(t0);
        FP_SECP256K1_norm(&t0);						//t0.norm(); //29
        FP_SECP256K1_mul(&z3,&z3,&t0);				//z3.mul(t0);//30
        FP_SECP256K1_sub(&(P->x),&x3,&z3);				//x3.sub(z3); //x3.norm();//31
        FP_SECP256K1_add(&t0,&t0,&t0);				//t0.add(t0);
        FP_SECP256K1_norm(&t0);						//t0.norm();//32
        FP_SECP256K1_add(&t1,&t1,&t1);				//t1.add(t1);
        FP_SECP256K1_norm(&t1);						//t1.norm();//33
        FP_SECP256K1_mul(&(P->z),&t0,&t1);				//z3.mul(t1);//34

        FP_SECP256K1_norm(&(P->x));					//x.norm();
        FP_SECP256K1_copy(&(P->y),&y3);				//y.copy(y3);
        FP_SECP256K1_norm(&(P->y));					//y.norm();
        FP_SECP256K1_norm(&(P->z));					//z.norm();
    }
#endif

#if CURVETYPE_SECP256K1==EDWARDS
    /* Not using square for multiplication swap, as (1) it needs more adds, and (2) it triggers more reductions */

    FP_SECP256K1 C,D,H,J;

    FP_SECP256K1_sqr(&C,&(P->x));							//C.sqr();

    FP_SECP256K1_mul(&(P->x),&(P->x),&(P->y));		//x.mul(y);
    FP_SECP256K1_add(&(P->x),&(P->x),&(P->x));		//x.add(x);
    FP_SECP256K1_norm(&(P->x));						//x.norm();

    FP_SECP256K1_sqr(&D,&(P->y));							//D.sqr();

    if (CURVE_A_SECP256K1==-1)				//if (ROM.CURVE_A==-1)
        FP_SECP256K1_neg(&C,&C);				//	C.neg();

    FP_SECP256K1_add(&(P->y),&C,&D);		//y.add(D);
    FP_SECP256K1_norm(&(P->y));				//y.norm();
    FP_SECP256K1_sqr(&H,&(P->z));				//H.sqr();
    FP_SECP256K1_add(&H,&H,&H);				//H.add(H);

    FP_SECP256K1_sub(&J,&(P->y),&H);			//J.sub(H);
    FP_SECP256K1_norm(&J);					//J.norm();

    FP_SECP256K1_mul(&(P->x),&(P->x),&J);		//x.mul(J);
    FP_SECP256K1_sub(&C,&C,&D);				//C.sub(D);
    FP_SECP256K1_norm(&C);					//C.norm();
    FP_SECP256K1_mul(&(P->z),&(P->y),&J);		//z.mul(J);
    FP_SECP256K1_mul(&(P->y),&(P->y),&C);		//y.mul(C);


#endif

#if CURVETYPE_SECP256K1==MONTGOMERY
    FP_SECP256K1 A,B,AA,BB,C;

    FP_SECP256K1_add(&A,&(P->x),&(P->z));			//A.add(z);
    FP_SECP256K1_norm(&A);					//A.norm();
    FP_SECP256K1_sqr(&AA,&A);				//AA.sqr();
    FP_SECP256K1_sub(&B,&(P->x),&(P->z));			//B.sub(z);
    FP_SECP256K1_norm(&B);					//B.norm();

    FP_SECP256K1_sqr(&BB,&B);				//BB.sqr();
    FP_SECP256K1_sub(&C,&AA,&BB);				//C.sub(BB);
    FP_SECP256K1_norm(&C);					//C.norm();
    FP_SECP256K1_mul(&(P->x),&AA,&BB);	//x.mul(BB);
    FP_SECP256K1_imul(&A,&C,(CURVE_A_SECP256K1+2)/4);	//A.imul((ROM.CURVE_A+2)/4);

    FP_SECP256K1_add(&BB,&BB,&A);				//BB.add(A);
    FP_SECP256K1_norm(&BB);					//BB.norm();
    FP_SECP256K1_mul(&(P->z),&BB,&C);		//z.mul(C);

#endif
}

#if CURVETYPE_SECP256K1==MONTGOMERY

/* Set P+=Q. W is difference between P and Q and is affine */
void ECP_SECP256K1_add(ECP_SECP256K1 *P,ECP_SECP256K1 *Q,ECP_SECP256K1 *W)
{
    FP_SECP256K1 A,B,C,D,DA,CB;

    FP_SECP256K1_add(&A,&(P->x),&(P->z));	//A.add(z);
    FP_SECP256K1_sub(&B,&(P->x),&(P->z));	//B.sub(z);

    FP_SECP256K1_add(&C,&(Q->x),&(Q->z));	//C.add(Q.z);

    FP_SECP256K1_sub(&D,&(Q->x),&(Q->z));	//D.sub(Q.z);
    FP_SECP256K1_norm(&A);			//A.norm();

    FP_SECP256K1_norm(&D);			//D.norm();
    FP_SECP256K1_mul(&DA,&D,&A);			//DA.mul(A);

    FP_SECP256K1_norm(&C);			//C.norm();
    FP_SECP256K1_norm(&B);			//B.norm();
    FP_SECP256K1_mul(&CB,&C,&B);		//CB.mul(B);

    FP_SECP256K1_add(&A,&DA,&CB);		//A.add(CB);
    FP_SECP256K1_norm(&A);			//A.norm();
    FP_SECP256K1_sqr(&(P->x),&A);			//A.sqr();
    FP_SECP256K1_sub(&B,&DA,&CB);		//B.sub(CB);
    FP_SECP256K1_norm(&B);			//B.norm();
    FP_SECP256K1_sqr(&B,&B);			//B.sqr();

    FP_SECP256K1_mul(&(P->z),&(W->x),&B);	//z.mul(B);

}

#else

/* Set P+=Q */
/* SU=248 */
void ECP_SECP256K1_add(ECP_SECP256K1 *P,ECP_SECP256K1 *Q)
{
#if CURVETYPE_SECP256K1==WEIERSTRASS

    int b3;
    FP_SECP256K1 t0,t1,t2,t3,t4,x3,y3,z3,b;

    if (CURVE_A_SECP256K1==0)
    {
        b3=3*CURVE_B_I_SECP256K1;					//int b=3*ROM.CURVE_B_I;
        FP_SECP256K1_mul(&t0,&(P->x),&(Q->x));		//t0.mul(Q.x);
        FP_SECP256K1_mul(&t1,&(P->y),&(Q->y));		//t1.mul(Q.y);
        FP_SECP256K1_mul(&t2,&(P->z),&(Q->z));		//t2.mul(Q.z);
        FP_SECP256K1_add(&t3,&(P->x),&(P->y));		//t3.add(y);
        FP_SECP256K1_norm(&t3);					//t3.norm();

        FP_SECP256K1_add(&t4,&(Q->x),&(Q->y));		//t4.add(Q.y);
        FP_SECP256K1_norm(&t4);					//t4.norm();
        FP_SECP256K1_mul(&t3,&t3,&t4);			//t3.mul(t4);
        FP_SECP256K1_add(&t4,&t0,&t1);			//t4.add(t1);

        FP_SECP256K1_sub(&t3,&t3,&t4);			//t3.sub(t4);
        FP_SECP256K1_norm(&t3);					//t3.norm();
        FP_SECP256K1_add(&t4,&(P->y),&(P->z));		//t4.add(z);
        FP_SECP256K1_norm(&t4);					//t4.norm();
        FP_SECP256K1_add(&x3,&(Q->y),&(Q->z));		//x3.add(Q.z);
        FP_SECP256K1_norm(&x3);					//x3.norm();

        FP_SECP256K1_mul(&t4,&t4,&x3);			//t4.mul(x3);
        FP_SECP256K1_add(&x3,&t1,&t2);			//x3.add(t2);

        FP_SECP256K1_sub(&t4,&t4,&x3);			//t4.sub(x3);
        FP_SECP256K1_norm(&t4);					//t4.norm();
        FP_SECP256K1_add(&x3,&(P->x),&(P->z));		//x3.add(z);
        FP_SECP256K1_norm(&x3);					//x3.norm();
        FP_SECP256K1_add(&y3,&(Q->x),&(Q->z));		//y3.add(Q.z);
        FP_SECP256K1_norm(&y3);					//y3.norm();
        FP_SECP256K1_mul(&x3,&x3,&y3);			//x3.mul(y3);

        FP_SECP256K1_add(&y3,&t0,&t2);			//y3.add(t2);
        FP_SECP256K1_sub(&y3,&x3,&y3);			//y3.rsub(x3);
        FP_SECP256K1_norm(&y3);					//y3.norm();
        FP_SECP256K1_add(&x3,&t0,&t0);			//x3.add(t0);
        FP_SECP256K1_add(&t0,&t0,&x3);			//t0.add(x3);
        FP_SECP256K1_norm(&t0);					//t0.norm();
        FP_SECP256K1_imul(&t2,&t2,b3);				//t2.imul(b);

        FP_SECP256K1_add(&z3,&t1,&t2);			//z3.add(t2);
        FP_SECP256K1_norm(&z3);					//z3.norm();
        FP_SECP256K1_sub(&t1,&t1,&t2);			//t1.sub(t2);
        FP_SECP256K1_norm(&t1);					//t1.norm();
        FP_SECP256K1_imul(&y3,&y3,b3);				//y3.imul(b);

        FP_SECP256K1_mul(&x3,&y3,&t4);			//x3.mul(t4);
        FP_SECP256K1_mul(&t2,&t3,&t1);			//t2.mul(t1);
        FP_SECP256K1_sub(&(P->x),&t2,&x3);			//x3.rsub(t2);
        FP_SECP256K1_mul(&y3,&y3,&t0);			//y3.mul(t0);
        FP_SECP256K1_mul(&t1,&t1,&z3);			//t1.mul(z3);
        FP_SECP256K1_add(&(P->y),&y3,&t1);			//y3.add(t1);
        FP_SECP256K1_mul(&t0,&t0,&t3);			//t0.mul(t3);
        FP_SECP256K1_mul(&z3,&z3,&t4);			//z3.mul(t4);
        FP_SECP256K1_add(&(P->z),&z3,&t0);			//z3.add(t0);

        FP_SECP256K1_norm(&(P->x));				//x.norm();
        FP_SECP256K1_norm(&(P->y));				//y.norm();
        FP_SECP256K1_norm(&(P->z));				//z.norm();
    }
    else
    {

        if (CURVE_B_I_SECP256K1==0)				//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_rcopy(&b,CURVE_B_SECP256K1);	//b.copy(new FP(new BIG(ROM.CURVE_B)));

        FP_SECP256K1_mul(&t0,&(P->x),&(Q->x));		//t0.mul(Q.x); //1
        FP_SECP256K1_mul(&t1,&(P->y),&(Q->y));		//t1.mul(Q.y); //2
        FP_SECP256K1_mul(&t2,&(P->z),&(Q->z));		//t2.mul(Q.z); //3

        FP_SECP256K1_add(&t3,&(P->x),&(P->y));		//t3.add(y);
        FP_SECP256K1_norm(&t3);					//t3.norm(); //4
        FP_SECP256K1_add(&t4,&(Q->x),&(Q->y));		//t4.add(Q.y);
        FP_SECP256K1_norm(&t4);					//t4.norm();//5
        FP_SECP256K1_mul(&t3,&t3,&t4);			//t3.mul(t4);//6

        FP_SECP256K1_add(&t4,&t0,&t1);			//t4.add(t1); //t4.norm(); //7
        FP_SECP256K1_sub(&t3,&t3,&t4);			//t3.sub(t4);
        FP_SECP256K1_norm(&t3);					//t3.norm(); //8
        FP_SECP256K1_add(&t4,&(P->y),&(P->z));		//t4.add(z);
        FP_SECP256K1_norm(&t4);					//t4.norm();//9
        FP_SECP256K1_add(&x3,&(Q->y),&(Q->z));		//x3.add(Q.z);
        FP_SECP256K1_norm(&x3);					//x3.norm();//10
        FP_SECP256K1_mul(&t4,&t4,&x3);			//t4.mul(x3); //11
        FP_SECP256K1_add(&x3,&t1,&t2);			//x3.add(t2); //x3.norm();//12

        FP_SECP256K1_sub(&t4,&t4,&x3);			//t4.sub(x3);
        FP_SECP256K1_norm(&t4);					//t4.norm();//13
        FP_SECP256K1_add(&x3,&(P->x),&(P->z));		//x3.add(z);
        FP_SECP256K1_norm(&x3);					//x3.norm(); //14
        FP_SECP256K1_add(&y3,&(Q->x),&(Q->z));		//y3.add(Q.z);
        FP_SECP256K1_norm(&y3);					//y3.norm();//15

        FP_SECP256K1_mul(&x3,&x3,&y3);			//x3.mul(y3); //16
        FP_SECP256K1_add(&y3,&t0,&t2);			//y3.add(t2); //y3.norm();//17

        FP_SECP256K1_sub(&y3,&x3,&y3);			//y3.rsub(x3);
        FP_SECP256K1_norm(&y3);					//y3.norm(); //18

        if (CURVE_B_I_SECP256K1==0)				//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_mul(&z3,&t2,&b);			//z3.mul(b); //18
        else
            FP_SECP256K1_imul(&z3,&t2,CURVE_B_I_SECP256K1);	//z3.imul(ROM.CURVE_B_I);

        FP_SECP256K1_sub(&x3,&y3,&z3);			//x3.sub(z3);
        FP_SECP256K1_norm(&x3);					//x3.norm(); //20
        FP_SECP256K1_add(&z3,&x3,&x3);			//z3.add(x3); //z3.norm(); //21

        FP_SECP256K1_add(&x3,&x3,&z3);			//x3.add(z3); //x3.norm(); //22
        FP_SECP256K1_sub(&z3,&t1,&x3);			//z3.sub(x3);
        FP_SECP256K1_norm(&z3);					//z3.norm(); //23
        FP_SECP256K1_add(&x3,&x3,&t1);			//x3.add(t1);
        FP_SECP256K1_norm(&x3);					//x3.norm(); //24

        if (CURVE_B_I_SECP256K1==0)				//if (ROM.CURVE_B_I==0)
            FP_SECP256K1_mul(&y3,&y3,&b);			//y3.mul(b); //18
        else
            FP_SECP256K1_imul(&y3,&y3,CURVE_B_I_SECP256K1);	//y3.imul(ROM.CURVE_B_I);

        FP_SECP256K1_add(&t1,&t2,&t2);			//t1.add(t2); //t1.norm();//26
        FP_SECP256K1_add(&t2,&t2,&t1);			//t2.add(t1); //t2.norm();//27

        FP_SECP256K1_sub(&y3,&y3,&t2);			//y3.sub(t2); //y3.norm(); //28

        FP_SECP256K1_sub(&y3,&y3,&t0);			//y3.sub(t0);
        FP_SECP256K1_norm(&y3);					//y3.norm(); //29
        FP_SECP256K1_add(&t1,&y3,&y3);			//t1.add(y3); //t1.norm();//30
        FP_SECP256K1_add(&y3,&y3,&t1);			//y3.add(t1);
        FP_SECP256K1_norm(&y3);					//y3.norm(); //31

        FP_SECP256K1_add(&t1,&t0,&t0);			//t1.add(t0); //t1.norm(); //32
        FP_SECP256K1_add(&t0,&t0,&t1);			//t0.add(t1); //t0.norm();//33
        FP_SECP256K1_sub(&t0,&t0,&t2);			//t0.sub(t2);
        FP_SECP256K1_norm(&t0);					//t0.norm();//34

        FP_SECP256K1_mul(&t1,&t4,&y3);			//t1.mul(y3);//35
        FP_SECP256K1_mul(&t2,&t0,&y3);			//t2.mul(y3);//36
        FP_SECP256K1_mul(&y3,&x3,&z3);			//y3.mul(z3);//37
        FP_SECP256K1_add(&(P->y),&y3,&t2);			//y3.add(t2); //y3.norm();//38
        FP_SECP256K1_mul(&x3,&x3,&t3);			//x3.mul(t3);//39
        FP_SECP256K1_sub(&(P->x),&x3,&t1);			//x3.sub(t1);//40
        FP_SECP256K1_mul(&z3,&z3,&t4);			//z3.mul(t4);//41

        FP_SECP256K1_mul(&t1,&t3,&t0);			//t1.mul(t0);//42
        FP_SECP256K1_add(&(P->z),&z3,&t1);			//z3.add(t1);
        FP_SECP256K1_norm(&(P->x));				//x.norm();

        FP_SECP256K1_norm(&(P->y));				//y.norm();
        FP_SECP256K1_norm(&(P->z));				//z.norm();
    }

#else
    FP_SECP256K1 A,B,C,D,E,F,G,b;

    FP_SECP256K1_mul(&A,&(P->z),&(Q->z));		//A.mul(Q.z);
    FP_SECP256K1_sqr(&B,&A);					//B.sqr();
    FP_SECP256K1_mul(&C,&(P->x),&(Q->x));		//C.mul(Q.x);
    FP_SECP256K1_mul(&D,&(P->y),&(Q->y));		//D.mul(Q.y);
    FP_SECP256K1_mul(&E,&C,&D);				//E.mul(D);

    if (CURVE_B_I_SECP256K1==0)			//if (ROM.CURVE_B_I==0)
    {
        FP_SECP256K1_rcopy(&b,CURVE_B_SECP256K1);	//FP b=new FP(new BIG(ROM.CURVE_B));
        FP_SECP256K1_mul(&E,&E,&b);			//E.mul(b);
    }
    else
        FP_SECP256K1_imul(&E,&E,CURVE_B_I_SECP256K1);	//E.imul(ROM.CURVE_B_I);

    FP_SECP256K1_sub(&F,&B,&E);			//F.sub(E);
    FP_SECP256K1_add(&G,&B,&E);			//G.add(E);

    if (CURVE_A_SECP256K1==1)				//if (ROM.CURVE_A==1)
    {
        FP_SECP256K1_sub(&E,&D,&C);		//E.sub(C);
    }
    FP_SECP256K1_add(&C,&C,&D);			//C.add(D);
    FP_SECP256K1_add(&B,&(P->x),&(P->y));		//B.add(y);

    FP_SECP256K1_add(&D,&(Q->x),&(Q->y));		//D.add(Q.y);
    FP_SECP256K1_norm(&B);				//B.norm();
    FP_SECP256K1_norm(&D);				//D.norm();
    FP_SECP256K1_mul(&B,&B,&D);			//B.mul(D);
    FP_SECP256K1_sub(&B,&B,&C);			//B.sub(C);
    FP_SECP256K1_norm(&B);				//B.norm();
    FP_SECP256K1_norm(&F);				//F.norm();
    FP_SECP256K1_mul(&B,&B,&F);			//B.mul(F);
    FP_SECP256K1_mul(&(P->x),&A,&B); //x.mul(B);
    FP_SECP256K1_norm(&G);				//G.norm();

    if (CURVE_A_SECP256K1==1)				//if (ROM.CURVE_A==1)
    {
        FP_SECP256K1_norm(&E);			//E.norm();
        FP_SECP256K1_mul(&C,&E,&G);		//C.mul(G);
    }
    if (CURVE_A_SECP256K1==-1)			//if (ROM.CURVE_A==-1)
    {
        FP_SECP256K1_norm(&C);			//C.norm();
        FP_SECP256K1_mul(&C,&C,&G);		//C.mul(G);
    }
    FP_SECP256K1_mul(&(P->y),&A,&C);	//y.mul(C);
    FP_SECP256K1_mul(&(P->z),&F,&G);	//z.mul(G);

#endif
}

/* Set P-=Q */
/* SU=16 */
void  ECP_SECP256K1_sub(ECP_SECP256K1 *P,ECP_SECP256K1 *Q)
{
    ECP_SECP256K1 NQ;
    ECP_SECP256K1_copy(&NQ,Q);
    ECP_SECP256K1_neg(&NQ);
    ECP_SECP256K1_add(P,&NQ);
}

#endif

#if CURVETYPE_SECP256K1!=MONTGOMERY
/* constant time multiply by small integer of length bts - use ladder */
void ECP_SECP256K1_pinmul(ECP_SECP256K1 *P,int e,int bts)
{
    int i,b;
    ECP_SECP256K1 R0,R1;

    ECP_SECP256K1_affine(P);
    ECP_SECP256K1_inf(&R0);
    ECP_SECP256K1_copy(&R1,P);

    for (i=bts-1; i>=0; i--)
    {
        b=(e>>i)&1;
        ECP_SECP256K1_copy(P,&R1);
        ECP_SECP256K1_add(P,&R0);
        ECP_SECP256K1_cswap(&R0,&R1,b);
        ECP_SECP256K1_copy(&R1,P);
        ECP_SECP256K1_dbl(&R0);
        ECP_SECP256K1_cswap(&R0,&R1,b);
    }
    ECP_SECP256K1_copy(P,&R0);
    ECP_SECP256K1_affine(P);
}
#endif

/* Set P=r*P */
/* SU=424 */
void ECP_SECP256K1_mul(ECP_SECP256K1 *P,BIG_256_28 e)
{
#if CURVETYPE_SECP256K1==MONTGOMERY
    /* Montgomery ladder */
    int nb,i,b;
    ECP_SECP256K1 R0,R1,D;
    if (ECP_SECP256K1_isinf(P)) return;
    if (BIG_256_28_iszilch(e))
    {
        ECP_SECP256K1_inf(P);
        return;
    }

    ECP_SECP256K1_copy(&R0,P);
    ECP_SECP256K1_copy(&R1,P);
    ECP_SECP256K1_dbl(&R1);

    ECP_SECP256K1_copy(&D,P);
    ECP_SECP256K1_affine(&D);

    nb=BIG_256_28_nbits(e);
    for (i=nb-2; i>=0; i--)
    {
        b=BIG_256_28_bit(e,i);
        ECP_SECP256K1_copy(P,&R1);
        ECP_SECP256K1_add(P,&R0,&D);
        ECP_SECP256K1_cswap(&R0,&R1,b);
        ECP_SECP256K1_copy(&R1,P);
        ECP_SECP256K1_dbl(&R0);

        ECP_SECP256K1_cswap(&R0,&R1,b);
    }

    ECP_SECP256K1_copy(P,&R0);

#else
    /* fixed size windows */
    int i,nb,s,ns;
    BIG_256_28 mt,t;
    ECP_SECP256K1 Q,W[8],C;
    sign8 w[1+(NLEN_256_28*BASEBITS_256_28+3)/4];

    if (ECP_SECP256K1_isinf(P)) return;
    if (BIG_256_28_iszilch(e))
    {
        ECP_SECP256K1_inf(P);
        return;
    }

    ECP_SECP256K1_affine(P);

    /* precompute table */

    ECP_SECP256K1_copy(&Q,P);
    ECP_SECP256K1_dbl(&Q);

    ECP_SECP256K1_copy(&W[0],P);

    for (i=1; i<8; i++)
    {
        ECP_SECP256K1_copy(&W[i],&W[i-1]);
        ECP_SECP256K1_add(&W[i],&Q);
    }

//printf("W[1]= ");ECP_output(&W[1]); printf("\n");

    /* make exponent odd - add 2P if even, P if odd */
    BIG_256_28_copy(t,e);
    s=BIG_256_28_parity(t);
    BIG_256_28_inc(t,1);
    BIG_256_28_norm(t);
    ns=BIG_256_28_parity(t);
    BIG_256_28_copy(mt,t);
    BIG_256_28_inc(mt,1);
    BIG_256_28_norm(mt);
    BIG_256_28_cmove(t,mt,s);
    ECP_SECP256K1_cmove(&Q,P,ns);
    ECP_SECP256K1_copy(&C,&Q);

    nb=1+(BIG_256_28_nbits(t)+3)/4;

    /* convert exponent to signed 4-bit window */
    for (i=0; i<nb; i++)
    {
        w[i]=BIG_256_28_lastbits(t,5)-16;
        BIG_256_28_dec(t,w[i]);
        BIG_256_28_norm(t);
        BIG_256_28_fshr(t,4);
    }
    w[nb]=BIG_256_28_lastbits(t,5);

    ECP_SECP256K1_copy(P,&W[(w[nb]-1)/2]);
    for (i=nb-1; i>=0; i--)
    {
        ECP_SECP256K1_select(&Q,W,w[i]);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_add(P,&Q);
    }
    ECP_SECP256K1_sub(P,&C); /* apply correction */
#endif
    ECP_SECP256K1_affine(P);
}

#if CURVETYPE_SECP256K1!=MONTGOMERY
/* Set P=eP+fQ double multiplication */
/* constant time - as useful for GLV method in pairings */
/* SU=456 */

void ECP_SECP256K1_mul2(ECP_SECP256K1 *P,ECP_SECP256K1 *Q,BIG_256_28 e,BIG_256_28 f)
{
    BIG_256_28 te,tf,mt;
    ECP_SECP256K1 S,T,W[8],C;
    sign8 w[1+(NLEN_256_28*BASEBITS_256_28+1)/2];
    int i,a,b,s,ns,nb;

    BIG_256_28_copy(te,e);
    BIG_256_28_copy(tf,f);

    /* precompute table */
    ECP_SECP256K1_copy(&W[1],P);
    ECP_SECP256K1_sub(&W[1],Q);  /* P+Q */
    ECP_SECP256K1_copy(&W[2],P);
    ECP_SECP256K1_add(&W[2],Q);  /* P-Q */
    ECP_SECP256K1_copy(&S,Q);
    ECP_SECP256K1_dbl(&S);  /* S=2Q */
    ECP_SECP256K1_copy(&W[0],&W[1]);
    ECP_SECP256K1_sub(&W[0],&S);
    ECP_SECP256K1_copy(&W[3],&W[2]);
    ECP_SECP256K1_add(&W[3],&S);
    ECP_SECP256K1_copy(&T,P);
    ECP_SECP256K1_dbl(&T); /* T=2P */
    ECP_SECP256K1_copy(&W[5],&W[1]);
    ECP_SECP256K1_add(&W[5],&T);
    ECP_SECP256K1_copy(&W[6],&W[2]);
    ECP_SECP256K1_add(&W[6],&T);
    ECP_SECP256K1_copy(&W[4],&W[5]);
    ECP_SECP256K1_sub(&W[4],&S);
    ECP_SECP256K1_copy(&W[7],&W[6]);
    ECP_SECP256K1_add(&W[7],&S);

    /* if multiplier is odd, add 2, else add 1 to multiplier, and add 2P or P to correction */

    s=BIG_256_28_parity(te);
    BIG_256_28_inc(te,1);
    BIG_256_28_norm(te);
    ns=BIG_256_28_parity(te);
    BIG_256_28_copy(mt,te);
    BIG_256_28_inc(mt,1);
    BIG_256_28_norm(mt);
    BIG_256_28_cmove(te,mt,s);
    ECP_SECP256K1_cmove(&T,P,ns);
    ECP_SECP256K1_copy(&C,&T);

    s=BIG_256_28_parity(tf);
    BIG_256_28_inc(tf,1);
    BIG_256_28_norm(tf);
    ns=BIG_256_28_parity(tf);
    BIG_256_28_copy(mt,tf);
    BIG_256_28_inc(mt,1);
    BIG_256_28_norm(mt);
    BIG_256_28_cmove(tf,mt,s);
    ECP_SECP256K1_cmove(&S,Q,ns);
    ECP_SECP256K1_add(&C,&S);

    BIG_256_28_add(mt,te,tf);
    BIG_256_28_norm(mt);
    nb=1+(BIG_256_28_nbits(mt)+1)/2;

    /* convert exponent to signed 2-bit window */
    for (i=0; i<nb; i++)
    {
        a=BIG_256_28_lastbits(te,3)-4;
        BIG_256_28_dec(te,a);
        BIG_256_28_norm(te);
        BIG_256_28_fshr(te,2);
        b=BIG_256_28_lastbits(tf,3)-4;
        BIG_256_28_dec(tf,b);
        BIG_256_28_norm(tf);
        BIG_256_28_fshr(tf,2);
        w[i]=4*a+b;
    }
    w[nb]=(4*BIG_256_28_lastbits(te,3)+BIG_256_28_lastbits(tf,3));

    ECP_SECP256K1_copy(P,&W[(w[nb]-1)/2]);
    for (i=nb-1; i>=0; i--)
    {
        ECP_SECP256K1_select(&T,W,w[i]);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_dbl(P);
        ECP_SECP256K1_add(P,&T);
    }
    ECP_SECP256K1_sub(P,&C); /* apply correction */
    ECP_SECP256K1_affine(P);
}

#endif

void ECP_SECP256K1_generator(ECP_SECP256K1 *G)
{
    BIG_256_28 x,y;
    BIG_256_28_rcopy(x,CURVE_Gx_SECP256K1);
#if CURVETYPE_SECP256K1!=MONTGOMERY
    BIG_256_28_rcopy(y,CURVE_Gy_SECP256K1);
    ECP_SECP256K1_set(G,x,y);
#else
    ECP_SECP256K1_set(G,x);
#endif
}

#ifdef HAS_MAIN

int main()
{
    int i;
    ECP_SECP256K1 G,P;
    csprng RNG;
    BIG_256_28 r,s,x,y,b,m,w,q;
    BIG_256_28_rcopy(x,CURVE_Gx);
#if CURVETYPE_SECP256K1!=MONTGOMERY
    BIG_256_28_rcopy(y,CURVE_Gy);
#endif
    BIG_256_28_rcopy(m,Modulus_SECP256K1);

    printf("x= ");
    BIG_256_28_output(x);
    printf("\n");
#if CURVETYPE_SECP256K1!=MONTGOMERY
    printf("y= ");
    BIG_256_28_output(y);
    printf("\n");
#endif
    RNG_seed(&RNG,3,"abc");

#if CURVETYPE_SECP256K1!=MONTGOMERY
    ECP_SECP256K1_set(&G,x,y);
#else
    ECP_SECP256K1_set(&G,x);
#endif
    if (ECP_SECP256K1_isinf(&G)) printf("Failed to set - point not on curve\n");
    else printf("set success\n");

    ECP_SECP256K1_output(&G);

    BIG_256_28_rcopy(r,CURVE_Order); //BIG_dec(r,7);
    printf("r= ");
    BIG_256_28_output(r);
    printf("\n");

    ECP_SECP256K1_copy(&P,&G);

    ECP_SECP256K1_mul(&P,r);

    ECP_SECP256K1_output(&P);
//exit(0);
    BIG_256_28_randomnum(w,&RNG);
    BIG_256_28_mod(w,r);

    ECP_SECP256K1_copy(&P,&G);
    ECP_SECP256K1_mul(&P,w);

    ECP_SECP256K1_output(&P);

    return 0;
}

#endif
