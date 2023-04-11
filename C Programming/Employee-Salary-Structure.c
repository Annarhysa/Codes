#include <stdio.h>
#include<stdlib.h>

struct Employee {
    char name[50];
    float hours_worked;
    float hourly_rate;
    float salary;
};

int main() {
    int num_employees;
    printf("Enter the number of employees: ");
    scanf("%d", &num_employees);

    struct Employee *employees = (struct Employee *)malloc(num_employees * sizeof(struct Employee));

    for (int i = 0; i < num_employees; i++) {
        printf("Enter the name of Employee %d: ", i+1);
        scanf("%s", employees[i].name);
        printf("Enter the number of hours worked by Employee %d: ", i+1);
        scanf("%f", &employees[i].hours_worked);
        printf("Enter the hourly rate of Employee %d: ", i+1);
        scanf("%f", &employees[i].hourly_rate);
    }

    for (int i = 0; i < num_employees; i++) {
        employees[i].salary = employees[i].hours_worked * employees[i].hourly_rate;
    }

    printf("\nEmployee Salaries:\n");
    for (int i = 0; i < num_employees; i++) {
        printf("Name: %s\n", employees[i].name);
        printf("Hours Worked: %.2f\n", employees[i].hours_worked);
        printf("Hourly Rate: $%.2f\n", employees[i].hourly_rate);
        printf("Salary: $%.2f\n", employees[i].salary);
        printf("\n");
    }

    free(employees);

    return 0;
}
