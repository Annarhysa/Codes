#include <stdio.h>
int main()
{int a1,a2,a3,c1,c2,c3; scanf("%d %d %d %d %d %d", &a1,&a2,&a3,&c1,&c2,&c3);
if (a1>a2 && a1>a3 && a2>a3) {if (c1>c2 && c1>c3 && c2>c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1<a2 && a1<a3 && a2<a3) {if (c1<c2 && c1<c3 && c2<c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1>a2 && a1>a3 && a2<a3) {if (c1>c2 && c1>c3 && c2<c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1<a2 && a1<a3 && a2>a3) {if (c1<c2 && c1<c3 && c2>c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a2>a1 && a2>a3 && a1>a3) {if (c2>c1 && c2>c3 && c1>c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a2<a1 && a2<a3 && a1<a3) {if (c2<c1 && c2<c3 && c1<c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a2>a1 && a2>a3 && a1<a3) {if (c2>c1 && c2>c3 && c1<c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a2<a1 && a2<a3 && a1>a3) {if (c2<c1 && c2<c3 && c1>c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a3>a1 && a3>a2 && a1>a2) {if (c3>c1 && c3>c2 && c1>c2)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a3<a1 && a3<a2 && a1<a2) {if (c3<c1 && c3<c2 && c1<c2)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a3>a1 && a3>a2 && a1<a2) {if (c3>c1 && c3>c2 && c1<c2)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a3<a1 && a3<a2 && a1>a2) {if (c3<c1 && c3<c2 && c1>c2)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1 == a2 && a1 == a3) {if (c1 == c2 && c1==c3)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1 == a2 && a3>a2) {if (c1 == c2 && c3>c2)
{printf("FAIR");}
else {printf("UNFAIR");}}
else if (a1 == a2 && a3<a2) {if (c1 == c2 && c3<c2)
{printf("FAIR");} else {printf("UNFAIR");}}
else if (a1 == a3 && a3>a2) {if (c1 == c3 && c3>c2)
{printf("FAIR");} else {printf("UNFAIR");}}
else if (a1 == a3 && a3<a2) {if (c1 == c3 && c3<c2)
{printf("FAIR");} else {printf("UNFAIR");}}
else if (a2 == a3 && a1<a2) {if (c2 == c3 && c1<c2)
{printf("FAIR");} else {printf("UNFAIR");}}
else if (a2 == a3 && a1>a2) {if (c2 == c3 && c1>c2)
{printf("FAIR");} else {printf("UNFAIR");}}
	return 0;}
