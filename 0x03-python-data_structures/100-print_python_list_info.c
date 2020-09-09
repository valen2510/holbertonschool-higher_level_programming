#include <Python.h>
#include <stdio.h>
/**
 * print_pyhton_list-info - prints info from a pyhton list using Cpyhton
 * @p: PyObject of the list
 **/
void print_python_list_info(PyObject *p)
{
	int counter;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (counter = 0; counter < PyList_Size(p); counter++)
		printf("Element %d: %s\n", counter, Py_TYPE(PyList_GetItem(p, counter))->tp_name);
}
