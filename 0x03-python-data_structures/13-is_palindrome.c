#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of a linked list
 *
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int nodes = 0;
	int i = 0;
	int j = 0;
	int list[9000];
	listint_t *tmp;

	tmp = *head;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (tmp != NULL)
	{
		list[nodes] = tmp->n;
		tmp = tmp->next;
		nodes++;
	}

	i = nodes - 1;

	while (i >= 0 && j <= i)
	{
		if (list[i] != list[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}
