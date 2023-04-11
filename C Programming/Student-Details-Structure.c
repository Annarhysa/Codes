#include <stdio.h>

struct Student {
    char name[50];
    int rollNo;
    float marks1;
    float marks2;
};

int main() {
    struct Student student;  
    struct Student *ptr;    

    ptr = &student;  

    printf("Enter name: ");
    scanf("%s", ptr->name);
    printf("Enter roll number: ");
    scanf("%d", &ptr->rollNo);
    printf("Enter marks: ");
    scanf("%f", &ptr->marks1);
    printf("Enter marks: ");
    scanf("%f", &ptr->marks2);

    
    printf("\nStudent Details:\n");
    printf("Name: %s\n", ptr->name);
    printf("Roll Number: %d\n", ptr->rollNo);
    printf("Marks: %.2f\n", (ptr->marks1+ptr->marks2)/2);

    return 0;
}
