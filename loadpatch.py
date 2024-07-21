import os

def Read(fileName: str):
    with open(fileName, "r") as file:
        data = file.read()
    return data

def Write(fileName: str, data: str):
    with open(fileName, "w") as file:
        file.write(data)

def Replace(fileName: str, before: str, after: str):
    data = Read(fileName)
    data.replace(before, after)
    Write(fileName, data)

for i in [
    [
        "dlls/crypt32/unixlib.c",
        '"/etc/security/cacerts",',
        '"/etc/security/cacerts", "@TERMUX_PREFIX@/etc/tls"'
    ],
    [
        "dlls/dbghelp/macho_module.c",
        'fallback = L"/usr/local/lib:/lib:/usr/lib";',
        'fallback = L"@TERMUX_PREFIX@/lib:/usr/local/lib:/lib:/usr/lib";'
    ],
    [
        "dlls/dbghelp/module.c",
        'p = malloc(sizeof(L"/usr/lib/debug/.build-id/") +',
        'p = malloc(sizeof(L"@TERMUX_PREFIX@//lib/debug/.build-id/") +'
    ],
    [
        "dlls/dbghelp/module.c",
        'wcscpy(p, L"/usr/lib/debug/.build-id/");',
        'wcscpy(p, L"@TERMUX_PREFIX@//lib/debug/.build-id/");'
    ],
    [
        "dlls/dbghelp/module.c",
        'sizeof(L"/usr/lib/debug/.build-id/") + (3 + filename_len + idlen * 2) * sizeof(WCHAR));");',
        'sizeof(L"@TERMUX_PREFIX@/lib/debug/.build-id/") + (3 + filename_len + idlen * 2) * sizeof(WCHAR));'
    ],
    [
        "dlls/dbghelp/module.c",
        'p = memcpy(dst, L"/usr/lib/debug/.build-id/", sizeof(L"/usr/lib/debug/.build-id/"));',
        'p = memcpy(dst, L"@TERMUX_PREFIX@/lib/debug/.build-id/", sizeof(L"@TERMUX_PREFIX@/lib/debug/.build-id/"));'
    ],
    [
        "dlls/msvcrt/tests/environ.c",
        '"/usr/lib/";',
        '"/usr/lib/;"\n"@TERMUX_PREFIX@/lib/"'
    ],
    [
        "dlls/ntdll/unix/server.c",
        "#ifdef __ANDROID__",
        "#if defined(__ANDROID__) && ! defined(__TERMUX__)"
    ],
    [
        "dlls/ntdll/unix/server.c",
        'asprintf( &dir, "/tmp/.wine-%u/server-%s", getuid(), tmp );',
        'asprintf( &dir, "@TERMUX_PREFIX@/tmp/.wine-%u/server-%s", getuid(), tmp );'
    ],
    [
        "programs/winebrowser/main.c",
        "/usr/bin/open\\0",
        "/usr/bin/open\\0@TERMUX_PREFIX@/bin/open\\0",
    ],
    [
        "programs/winemenubuilder/winemenubuilder.c",
        'dirs = xwcsdup( L"/usr/local/share/:/usr/share/" );',
        'dirs = xwcsdup( L"@TERMUX_PREFIX@/share:/usr/local/share/:/usr/share/" );'
    ],
    [
        "server/request.c",
        "#ifdef __ANDROID__",
        "#if defined(__ANDROID__) && ! defined(__TERMUX__)"
    ],
    [
        "server/request.c",
        'len += sizeof("/tmp/.wine-") + 12;',
        'len += sizeof("@TERMUX_PREFIX@/tmp/.wine-") + 12;'
    ],
    [
        "server/request.c",
        'sprintf( server_dir, "/tmp/.wine-%u", getuid() );',
        'sprintf( server_dir, "@TERMUX_PREFIX@/tmp/.wine-%u", getuid() );'
    ],
    [
        "dlls/ntdll/unix/loader.c",
        "#ifdef __ANDROID__",
        "#if defined(__ANDROID__) && ! defined(__TERMUX__)"
    ],
    [
        "dlls/ntdll/unix/loader.c",
        "#if (defined(__linux__) && !defined(__ANDROID__)) || defined(__FreeBSD_kernel__) || defined(__NetBSD__)",
        "#if (defined(__linux__) && !(defined(__ANDROID__) && ! defined(__TERMUX__))) || defined(__FreeBSD_kernel__) || defined(__NetBSD__)"
    ],
    [
        "dlls/ntdll/unix/socket.c",
        "# ifdef SOL_IPX",
        "# if defined(SOL_IPX) && !defined(__ANDROID__)"
    ],
    [
        "dlls/ws2_32/unixlib.c",
        "# ifdef SOL_IPX",
        "# if defined(SOL_IPX) && !defined(__ANDROID__)"
    ],
    [
        "server/sock.c",
        "# ifdef SOL_IPX",
        "# if defined(SOL_IPX) && !defined(__ANDROID__)"
    ],
    [
        "tools/winebuild/utils.c",
        "int using_cc = 0;",
        "int using_cc = 1;"
    ],
    [
        "tools/winegcc/winegcc.c",
        'strarray_add( &ret, "-target" );',
        '''            if (strstr(opts->target_alias, "android")) {
                if (strstr(opts->target_alias, "arm")) {
                    str = strmake( "%s24", "armv7a-linux-androideabi" );
                } else {
                    str = strmake( "%s24", opts->target_alias );
                }
            } else {
                str = strmake( "%s", opts->target_alias );
            }
             strarray_add( &ret, "-target" );'''
    ],
    [
        "tools/winegcc/winegcc.c",
        'strarray_add( &ret, opts->target_alias );',
        'strarray_add( &ret, str );'
    ]
]:
    Replace(i[0], i[1], i[2])

