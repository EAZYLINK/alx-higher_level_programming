#include "lists.h"

/**
 * insert_number - inserts a node to a list
 * @head: node head
 * @number: number of nodes
 * Return: listint_t
 */

listint_t *insert_number(listint_t **head, int number)
{
listint_t *new;
listint_t *current;
current = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
if (*head == NULL)
*head = new;
else
{
while (current->next != NULL)
current = current->next;
current->next = new;
}
return (new);
}
