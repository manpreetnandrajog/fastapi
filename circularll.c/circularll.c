#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;

}
// create new node and insertion
void insert(struct node *next)
int ( node *head, item);
node head *temp, *rear);
if head == null;
printf("list is empty");
 temp= head ;
 rear= temp;
// for non empty list
temp->next= head;
head=temp;
rear -> next= head;

// display cll
void printlist(struct node *next);
{
    while(n!=null)
    {
        printf( "%d", n->data);
        n = n ->next;
    }
}
// delete cll
void delete(struct node *next);
{
    temp=head;
    head= head->next;
    rear -> next = head;
    free temp;


}



int main()
{
    struct node *head = NULL;
    struct node *second = NULL;
    struct node *third = NULL;
    head = (struct node*) malloc (size of (struct node));
    second=  (struct node*) malloc (size of (struct node));
    third=  (struct node*) malloc (size of (struct node));

    head -> data= 1;
    head -> next = second;
    second -> data= 8;
    second -> next = third;
   third -> data= 7;
   third -> next = head;

   insert();
   printlist(head);
   delete();
   return 0;

    
}