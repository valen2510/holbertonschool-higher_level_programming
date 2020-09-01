#include "lists.h"
/**
 * check_cycle - check if a linkes list has a cycle in it
 * @list: list
 * Return: 0 (No cycle in the list) 1 (Cycle in the list)
 **/
int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *bunny;

	if (!list || !list->next)
		return (0);

	turtle = list;
	bunny = turtle->next->next;

	while (turtle && bunny && bunny->next)
	{
		if (turtle == bunny)
			return (1);

		bunny = bunny->next->next;
		turtle = turtle->next;

	}
	return (0);
}
