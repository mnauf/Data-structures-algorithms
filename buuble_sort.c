#include <stdio.h>
int main(void)
{
int k,ptr,temp,a[7]={10,6,7,5,9,4,8};
printf("The unmodified list is as follows: "):
for (i=0;i<=6;i++)
{
printf("%d, ",a[i]);
}
for (k=1;k<=7-1;k++)
{
for (ptr=0;ptr<=6-k;ptr++)
{
if (a[ptr]>=a[ptr+1])
{
temp=a[ptr];
a[ptr]=a[ptr+1];
a[ptr+1]=temp;
}
}
}
for (ptr=0;ptr<=6;ptr++)
printf("%d ",a[ptr]);
return 0;
}
