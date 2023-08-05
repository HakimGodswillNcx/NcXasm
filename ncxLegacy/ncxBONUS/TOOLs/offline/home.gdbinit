define init-peda
source /home/ncx/peda/peda.py
end
document init-peda
Initializes the PEDA (Python Exploit Development Assistant for GDB) framework
end

define init-pwndbg
source /home/ncx/Downloads/pwndbg/gdbinit.py
end
document init-pwndbg
Initializes PwnDBG
end

define init-gef
source /home/ncx/.gef-a85368fc771dcbb4db2b41818781e182845015b9.py
end
document init-gef
Initializes GEF (GDB Enhanced Features)
end

set auto-load safe-path /
set solib-search-path /usr/lib/x86_64-linux-gnu/
set libthread-db-search-path /usr/lib/x86_64-linux-gnu
