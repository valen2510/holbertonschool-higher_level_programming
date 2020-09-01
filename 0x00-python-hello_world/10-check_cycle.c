#include "lists.h"
/**
 * check_cycle - check if a linkes list has a cycle in it
 * @list: list
 * Return: 0 (No cycle in the list) 1 (Cycle in the list)
 **/
int check_cycle(listint_t *list)
{
	listint_t *aux_list;
	listint_t *next_node;

	if (!list)
		return (-1);

	aux_list = list;
	next_node = aux_list->next;

	while (aux_list)
	{
		while (next_node)
		{
			if (next_node->next == aux_list)
				return (1);

			next_node = next_node->next;
		}

		if (!next_node)
			break;

		aux_list = aux_list->next;

	}
	return (0);
}
