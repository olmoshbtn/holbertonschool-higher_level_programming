#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current == NULL || number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current != NULL)
	{
		if (number > current->n)
		{
			previous = current;
			current = current->next;
		}
		else
			break;
	}

	previous->next = new;
	new->next = current;
	return (new);
}