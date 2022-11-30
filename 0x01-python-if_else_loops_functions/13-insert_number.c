#include "lists.h"

/**
 * insert_node - inserts a node to a list
 * @head: node head
 * @number: number of nodes
 * Return: listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;
current = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL || (*head)->n > number)
{
new->next = *head;
*head = new;
return (new);
}
while (current->next != NULL)
if ((current->next)->n >= number)
{
new->next = current->next;
current->next = new;
return (new);
}
current = current->next;
}
current->next = new;
new->next = NULL;
return (new);
}
