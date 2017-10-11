#include <stdarg.h>
#include "module.h"

typedef int (*python_fiber_run_f)(void*, void*);

int python_fiber_run_bridge_f(va_list ap) {
  python_fiber_run_f cb = va_arg(ap, python_fiber_run_f);
  void* function = va_arg(ap, void*);
  void* arg = va_arg(ap, void*);

  cb(function, arg);

  return 0;
}

int python_fiber_create(python_fiber_run_f cb, void* function, void* args) {
  struct fiber *f = fiber_new("python", python_fiber_run_bridge_f);

  if (f == NULL) {
    return -1;
  }

  fiber_start(f, cb, function, args);

  return 0;
}
