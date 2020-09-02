#include "lists.h"
/**
* insert_node - insert a number in a single linked list
* @head: list
* @number: number in list
* Return: new_node (Success) NULL (Fail)
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *aux_head = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	aux_head = *head;
	while (aux_head)
	{
		if (aux_head->next->n > new_node->n)
			break;
		aux_head = aux_head->next;
		if (!aux_head->next)
			break;
	}
	new_node->next = aux_head->next;
	aux_head->next = new_node;

	return (new_node);
}
