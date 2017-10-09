/* Example of a C submodule for Tarantool */
#include <tarantool/module.h>

#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

extern void dofile_python(const char* filename);

/* internal function */
static int
dofile(struct lua_State *L)
{
    if (lua_gettop(L) < 1)
        luaL_error(L, "Usage: dofile(filename)");

    const char* filename = lua_tostring(L, 1);

    dofile_python(filename);

    return 0;
}

/* exported function */
LUA_API int
luaopen_python(lua_State *L)
{
    /* result returned from require('ckit.lib') */
    lua_newtable(L);
    static const struct luaL_Reg meta [] = {
        {"dofile", dofile},
        {NULL, NULL}
    };
    luaL_register(L, NULL, meta);
    return 1;
}
/* vim: syntax=c ts=8 sts=8 sw=8 noet */
