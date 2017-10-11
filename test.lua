#!/usr/bin/env tarantool

local python = require('python')
local fiber = require('fiber')

local function foo()
    for i = 1,3 do
        python.dofile('test.py')
        fiber.sleep(1)
    end
end

fiber.create(foo)
fiber.create(foo)


--python.dofile('test.py')
