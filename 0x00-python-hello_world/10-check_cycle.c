#include "lists.h"

/**
 * check_cycle: function checks if a singly linked list has a cycle in it.
 * list: pointer to a list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	if (!list)
		return (0);

	while (turtle->next != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next;

		if (hare->next == NULL)
		{
			return (0);
		}
		hare = hare->next;
		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
