typedef ... va_list;
typedef ... fiber;

typedef int (*fiber_func)(va_list);

extern void fiber_sleep(double s);
extern bool fiber_is_cancelled();

struct fiber * fiber_new(const char *name, fiber_func f);


typedef int (*python_fiber_run_f)(void*, void*);

extern "Python" int python_fiber_run(void* function, void* args);

extern int python_fiber_create(python_fiber_run_f cb, void* function, void* args);
