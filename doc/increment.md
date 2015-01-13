
# aerospike.Client.increment

aerospike.Client.increment - Increments a numeric value in a bin

## Description

```
status = aerospike.Client.increment ( key, bin, offset [, initial_value = 0,
        policies ] )

```

**aerospike.Client.increment()** will increment a *bin* containing a numeric
value by the *offset* or set it to the *initial_value* if it does not exist.

## Parameters

**key**, the key for the record. A tuple with keys
['ns','set','key'] or ['ns','set','digest'].   

```
Tuple:
    key = ( <namespace>, 
            <set name>, 
            <the primary index key>, 
            <a RIPEMD-160 hash of the key, and always present> )

```

**bin**, the name of the bin.

**offset**, the integer by which to increment the value in the bin.

**policies**, the dictionary of policies to be given while increment.   

## Return Values
Returns an integer status. 0(Zero) is success value. In case of error, appropriate exceptions will be raised.

## Examples

```python

# -*- coding: utf-8 -*-
import aerospike
config = {
            'hosts': [('127.0.0.1', 3000)]
         }
client = aerospike.client(config).connect()

key = ('test', 'demo', 1)

options = {
    'timeout' : 5000,
    'key' : aerospike.POLICY_KEY_SEND
}

status = client.increment( key, bin, 5, 2, options)

print status


```

We expect to see:

```python
0
```



### See Also



- [Glossary](http://www.aerospike.com/docs/guide/glossary.html)

- [Aerospike Data Model](http://www.aerospike.com/docs/architecture/data-model.html)
