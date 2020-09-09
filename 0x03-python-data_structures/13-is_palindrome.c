#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - function to check if a single list is palindrome
 * @head: head of the list
 * Return: 1 (Palindrome) 0 (Not palindrome)
 **/
int is_palindrome(listint_t **head)
{
	unsigned int elements = number_elements(*head), iterations = 0;
	listint_t *aux_head = *head, *tail = NULL;

	if (elements == 0)
		return (1);
	if (elements % 2 == 0)
	{
		for (iterations = elements / 2; iterations > 0; iterations--)
		{
			tail = aux_head;
			elements = iterations * 2 - 1;
			printf("%d\n", elements);
			while (elements > 0)
				tail = tail->next, elements--;
			printf("%d\n", tail->n);
			if (aux_head->n != tail->n)
				return (0);
			aux_head = aux_head->next;
		}
		return (1);
	}
		for (iterations = (elements / 2) + 1; iterations > 0; iterations--)
		{
			tail = aux_head;
			elements = iterations * 2 - 1;
			while (elements > 1)
				tail = tail->next, elements--;
			if (aux_head->n != tail->n)
				return (0);
			aux_head = aux_head->next;
		}
		return (1);
}
/**
 * number_elements - find the number of elements in a list
 * @head: head of the list
 * Return: Conter (Number of elements)
 **/
unsigned int number_elements(listint_t *head)
{
	unsigned int counter = 0;

	while (head)
	{
		counter++;
		head = head->next;
	}
	return (counter);
}
