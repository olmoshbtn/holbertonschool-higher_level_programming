#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of a linked list
 *
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin = *head, *tail = *head;
	int forward = 0, backward = 0, nodes = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)      
		return (1);

	while (tail->next != NULL)
	{
		tail = tail->next;
		++nodes;
	}

	backward = nodes;

	while (backward >= forward)
	{
		if (tail->n != begin->n)
			return (0);
		tail -= 2;
		begin += 2;
		backward--;
		forward++;
	}
	return (1);
}
