#include <Python.h>
#include <objet.h>
#include <listobjet.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, PyTYPE(obj->ob_item[i])->tp_name);
}
