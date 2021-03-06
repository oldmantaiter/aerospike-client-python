# -*- coding: utf-8 -*-
################################################################################
# Copyright 2013-2014 Aerospike, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

from __future__ import print_function

import aerospike
import sys

from optparse import OptionParser

################################################################################
# Options Parsing
################################################################################

usage = "usage: %prog [options] [REQUEST]"

optparser = OptionParser(usage=usage, add_help_option=False)

optparser.add_option(
    "--help", dest="help", action="store_true",
    help="Displays this message.")

optparser.add_option(
    "-h", "--host", dest="host", type="string", default="127.0.0.1", metavar="<ADDRESS>",
    help="Address of Aerospike server.")

optparser.add_option(
    "-p", "--port", dest="port", type="int", default=3000, metavar="<PORT>",
    help="Port of the Aerospike server.")

(options, args) = optparser.parse_args()

if options.help:
    optparser.print_help()
    print()
    sys.exit(1)

################################################################################
# Client Configuration
################################################################################

config = {
    'hosts': [ (options.host, options.port) ]
}

################################################################################
# Application
################################################################################

exitCode = 0

try:

    # ----------------------------------------------------------------------------
    # Connect to Cluster
    # ----------------------------------------------------------------------------

    client = aerospike.client(config).connect()

    # ----------------------------------------------------------------------------
    # Perform Operation
    # ----------------------------------------------------------------------------

    try:

        request = "statistics"

        if len(args) > 0:
            request = ' '.join(args)

        for node,(err,res) in client.info(request).items():
            if res != None:
                res = res.strip()
                if len(res) > 0:
                    entries = res.split(';')
                    if len(entries) > 1:
                        print("{0}:".format(node))
                        for entry in entries:
                            entry = entry.strip()
                            if len(entry) > 0:
                                count = 0
                                for field in entry.split(','):
                                    (name,value) = field.split('=')
                                    if count > 0:
                                        print("      {0}: {1}".format(name, value))
                                    else:
                                        print("    - {0}: {1}".format(name, value))
                                    count += 1
                    else:
                        print("{0}: {1}".format(node, res))

    except Exception as e:
        print("error: {0}".format(e), file=sys.stderr)
        exitCode = 2

    # ----------------------------------------------------------------------------
    # Close Connection to Cluster
    # ----------------------------------------------------------------------------

    client.close()

except Exception, eargs:
    print("error: {0}".format(eargs), file=sys.stderr)
    exitCode = 3

################################################################################
# Exit
################################################################################

sys.exit(exitCode)
