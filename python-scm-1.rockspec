package = 'python'
version = 'scm-1'

source  = {
    url    = 'git://github.com/tarantool/python.git';
    branch = 'master';
}

description = {
    summary  = "Python support for Tarantool";
    homepage = 'https://github.com/tarantool/python.git';
    maintainer = "Konstantin Nazarov <racktear@tarantool.org>";
    license  = 'BSD2';
}

dependencies = {
    'lua == 5.1';
}

external_dependencies = {
    TARANTOOL = {
        header = 'tarantool/module.h';
    };
}

build = {
    type = 'cmake';
    variables = {
        CMAKE_BUILD_TYPE="RelWithDebInfo";
        TARANTOOL_INSTALL_LIBDIR="$(LIBDIR)";
        TARANTOOL_INSTALL_LUADIR="$(LUADIR)";
    };
}
-- vim: syntax=lua ts=4 sts=4 sw=4 et
