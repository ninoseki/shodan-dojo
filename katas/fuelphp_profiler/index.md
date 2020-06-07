# FuelPHP Profiler

Create a query to find hosts which use [FuelPHP](https://fuelphp.com/)'s [Profiler](https://fuelphp.com/docs/general/profiling.html).

## Background & hints

Many PHP Web application frameworks have a web based debugging console.

- CakePHP: [Debug Kit](https://book.cakephp.org/debugkit/4/en/index.html)
- FuelPHP: Profiler
- Phalcon: [Debug component](https://docs.phalcon.io/3.4/en/debug)
- Sympfony: [Profiler](https://symfony.com/doc/current/profiler.html)

The web based debugging console is useful, but it might cause a sensitive information leakage when it is enabled in production.

![](https://i.imgur.com/Vr4IBEZ.png)

In FuelPHP, the debugging console is called Profiler and it is based on [PHP-Quick-Profiler](https://github.com/wufoo/PHP-Quick-Profiler).

You can find query candidates in the code base.

![](https://i.imgur.com/ACkHEzp.png)
