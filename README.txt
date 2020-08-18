How to use:
python3 MalwareDetection.py <input directory>

output file : prediction.csv

Libraries:
- sklearn
- numpy
- pickle 0.23 version
- codecs, os, csv, os, math

Features Used:
|
1)Static files:
|
'Machine:', 'SizeOfOptionalHeader:', 'Characteristics:', 'MajorLinkerVersion:', 'MinorLinkerVersion:', 'SizeOfCode:', 'SizeOfInitializedData:', 'SizeOfUninitializedData:', 'AddressOfEntryPoint:', 'BaseOfCode:', 'BaseOfData:', 'ImageBase:', 'SectionAlignment:', 'FileAlignment:', 'MajorOperatingSystemVersion:', 'MinorOperatingSystemVersion:', 'MajorImageVersion:', 'MinorImageVersion:', 'MajorSubsystemVersion:', 'MinorSubsystemVersion:', 'SizeOfImage:', 'SizeOfHeaders:', 'CheckSum:', 'Subsystem:', 'DllCharacteristics:', 'SizeOfStackReserve:', 'SizeOfStackCommit:', 'SizeOfHeapReserve:', 'SizeOfHeapCommit:', 'LoaderFlags:', 'NumberOfRvaAndSizes:'
'SectionsNb:', 'SectionsMeanEntropy:', 'SectionsMinEntropy:', 'SectionsMaxEntropy:', 'SectionsMeanRawsize:', 'SectionsMinRawsize:', 'SectionMaxRawsize:', 'SectionsMeanVirtualsize:', 'SectionsMinVirtualsize:', 'SectionMaxVirtualsize:'
'ImportsNbDLL:', 'ImportsNbOrdinal'
|
2)Dynamic files:
|
"duration", "tls-request", "udp-request", "dns-request", "http-request", "icmp-request", "smtp-request", "tcp-request", "hosts", "domains", "irc-request"
"file_created", "file_recreated", "dll_loaded", "file_opened", "file_read", "file_written", "regkey_opened", "regkey_read"
"synchronisation-api", "system-api", "__notification__", "certificate-api", "netapi-api", "file-api", "misc-api", "process-api", "ole-api", "registry-api", "services-api", "network-api", "resource-api", "ui-api", "crypto"-api, "exception-api", "iexplore-api"


