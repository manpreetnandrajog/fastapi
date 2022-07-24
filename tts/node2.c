//node insert 10,20,30
#include<stdio.h>
struct node
{
int data;
struct node *next ;
}
*new, *head,*tail;
do
{
    new = malloc(size of (structure));
    scanf("%d",&value);
    new->data=value;
    new->next= null;
    if(head==null)
    {
        head=new;
        tail=new;
      }
      else
      {
          tail -> next=new;
          tail=new;
      }
      printf("y-continue&n-exit");
      scanf("%c",&ch)
}
while(ch=='y');
while(temp!=null)
{
    printf("%d", temp->data);
    temp= temp -> next ;
}
}

