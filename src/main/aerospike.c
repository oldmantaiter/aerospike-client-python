/*******************************************************************************
 * Copyright 2013-2014 Aerospike, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/

#include <Python.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#include "client.h"
#include "key.h"
#include "query.h"
#include "scan.h"
#include "predicates.h"

static PyMethodDef Aerospike_Methods[] = {

	{"client",		(PyCFunction) AerospikeClient_New,	METH_VARARGS | METH_KEYWORDS, 
					"Create a new instance of Client class."},	
	
	{NULL}
};

PyMODINIT_FUNC initaerospike()
{
	// Makes things "thread-safe"
	PyEval_InitThreads();

	// aerospike Module
	PyObject * aerospike = Py_InitModule3("aerospike", Aerospike_Methods, 
		"Aerospike Python Client");
	
	PyTypeObject * client = AerospikeClient_Ready();
	Py_INCREF(client);
	PyModule_AddObject(aerospike, "Client", (PyObject *) client);

	PyTypeObject * key = AerospikeKey_Ready();
	Py_INCREF(key);
	PyModule_AddObject(aerospike, "Key", (PyObject *) key);

	PyTypeObject * query = AerospikeQuery_Ready();
	Py_INCREF(query);
	PyModule_AddObject(aerospike, "Query", (PyObject *) query);

	PyTypeObject * scan = AerospikeScan_Ready();
	Py_INCREF(scan);
	PyModule_AddObject(aerospike, "Scan", (PyObject *) scan);

	PyObject * predicates = AerospikePredicates_New();
	PyModule_AddObject(aerospike, "predicates", predicates);
}
