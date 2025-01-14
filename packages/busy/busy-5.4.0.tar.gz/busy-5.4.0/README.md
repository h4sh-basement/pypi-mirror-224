Busy
====

Personal time management for techies
------------------------------------

tl;dr:

```bash
pipx install busy
```

```bash
busy
```

**Note: Busy versions 5.0 and later use a different data model from versions 3 and before. There's a conversion script, which must be run using regular Python. Also, many of the commands' behaviour and options have changed.**

_Using Busy? [Contact us!](mailto:busy@steampunkwizard.ca)_

Busy is a personal time management tool, designed to help us all through our crazy busy days with as little stress as possible. It's simple, fast, and fun to use.

Usage
=====

Principles
----------

Busy is built with the following usage principles in mind:

- *Monotasking*: We each focus better when we work on exactly one task at a time. So busy only shows you one task.
- *Keyboard-driven*: Productive people use the keyboard effectively, because muscle memory builds up over time, and it's faster to hit a key than to find an icon on a screen and move the pointer.
- *Offline use*: It's designed to run on your laptop or desktop computer, without needing an internet connection, so it works extremely fast under any conditions.
- *Multi-platform* Because Busy is a terminal-based application, it will run on MacOS, Linux, or Windows.
- *Personal*: Busy is not a collaboration platform or project management application. It's for managing your personal time, not assigning things to others.
- *Importance over Urgency*: Stop stressing out over last-minute tasks and impending deadlines! Busy makes it easy to capture future tasks and remember to do them early enough to reduce the pressure.
- *Editable data*: The data is stored in text files, which can easily be edited outside of Busy itself. (In fact, Busy started as a todo.txt type of approach and grew from there.)

_The idea of Importance over Urgency comes from the book "The 7 Habits of Highly Effective People". Although we firmly disagree with Steven Covey's statements on gay rights, the book contains excellent ideas._

Installation
------------


You'll need a terminal emulator to access a command or shell prompt. Examples include:

- iTerm2 or Terminal on MacOS
- Gnome Terminal or XTerm on Linux
- CMD on Windows
- Terminator on all platforms

Busy requires `pipx`, which requires Python 3.6 or later. To check whether you already have the right version of Python on your system, start your terminal emulator and type:

```
python3 -V
```

If you don't have Python, or your version is out of date, install or upgrade it. In most cases, you'll want to do so using your system's package manager (such as Homebrew on MacOS or APT on Ubuntu). If you're not familiar with package managers, then download Python from [the Python.org site](https://www.python.org/downloads/) directly and follow the instructions provided there. When done, use the version check above to confirm it's installed and the version is 3.6.5 or greater.

Python comes with PIP, which enables installation of Python packages from a central server called PyPI.

Once Python and PIP are installed, type:

```
pip3 install pipx
pipx install busy
```

To upgrade it later:

```
pipx upgrade busy
```

Overview
--------

Busy ships with two user interfaces, both of them terminal-based and keyboard-driven:

- *Shell UI* - A command-line interface (CLI) using shell conventions and called directly from the shell, one command at a time.
- *Curses UI* - A faster, more visual interface with one-key commands that remains visible the entire time it's being used.

Some commands also use your favorite terminal-based text editor, such as Emacs, vi, or Nano. It's possible to use Busy without a text editor, but functionality is limited.

Busy's core model is a collection of Items, which are typically tasks but can also be discussion topics, groceries to buy, or anything else you like. Items are organized into Queues, which are named sets of Items to do. You work on the top Item in a Queue, and when it's done, that Item gets marked as "done", to reveal the next one. There is a default Queue (called "tasks") but you can also create other Queues, for example a shopping list or discussion list.

Busy actually moves Items between States within each Queue. Each Queue contains a Collection (ordered list) of Items for each State. The States are:

- `todo`: Current Items for you to work on, discuss, or buy now.
- `done`: Items that have been done, with the date completed.
- `plan`: Items that have been deferred to a future date, with that date.

Using the Shell UI
------------------

To get started, add some tasks to your default Queue.

```
busy add --description "Donate to the Busy project"
busy add --description "Phone mom"
busy add --description "Do the laundry"
busy add --description "Take a shower"
```

Then, when you're ready to start your day, ask Busy what to do first:

```
busy show
```

Returns:

```
Take a shower
```

That's the last Item you added, because Busy adds items to the top of the queue, turning it into a [LIFO stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type).

When you've finished that task, mark it off to find the next task.

```
busy finish
```

It will ask you to confirm that you're done. Then request the next task:

```
busy show
```

Which will tell you what to do next:

```
Do the laundry
```

If you want to see the whole Queue, with sequence numbers, type:

```
busy list
```

Here's the list you will see. Note that the completed Task is gone:

```
1  Do the laundry
2  Phone mom
3  Donate to the Busy project
```

If you decide, in the moment, to wait until later today to perform a task, drop it to the bottom of the Queue using the `drop` command:

```
busy drop
```

Then `busy list` will return:

```
1  Phone mom
2  Donate to the Busy project
3  Do the laundry
```

If you see a task on the list that seems urgent, and you intend to perform it immediately, pop it to the top of the list:

```
busy pop --criteria 2
```

_Our use of the term "pop" for a command doesn't quite fit with the computing term "pop". It might change in the future._

Then `busy show` will return:

```
Donate to the Busy project
```

Let's say you realize that it's not an appropriate task for today, but you want to defer it to tomorrow:

```
busy defer
```

It will ask you to confirm "tomorrow" as the day for deferral. Agree with it for now. The Item will then be moved into the `plan` State with tomorrow's date as the plan date.

At the start of a new day, tell Busy to add all the previously deferred Items to the current Queue:

```
busy activate
```

Commands
--------

Here's a summary of the commands in Busy.

- `add` adds a new item to the top of the queue. The item description may be included after the command or typed on the next line.
- `show` gets the top item in the queue, referred to as the "current" item.
- `resource` shows the URL (if any) prefixed with an "@" symbol
- `base` is like `show`, but removes resources, followons, and tags
- `list` lists the items in the queue in order with their sequence numbers.
- `pop` moves a task or set of items to the top of a queue.
- `drop` moves a task or set of items to the bottom of a queue.
- `delete` permanently removes a task or set of items from a queue.
- `edit` opens a text editor to edit items - the default is to edit only the top item.
- `manage` is the same as `edit`, but defaults to edit the whole collection.
- `finish` moves a task or tasks from the `todo` state to the `done` state, so it's complete. Good job!
- `defer` moves a task or set of tasks from the `todo` state and schedules it or them to reappear at a future date in the `plan` state.
- `activate` moves current tasks from the `plan` state to the `todo` state. Get to work!
- `queues` to list all the queues.
- `tags` to list all the tags.
- `curses` launches the Curses UI, and is also the default if no command is provided.

Here are some of the options which apply to some or all of the commands:

- A queue name, which does not need an option designation
- `--help` to find out which options apply
- `--criteria` to designate items to be acted upon, using sequence numbers or tags
- `--yes` to skip confirmation of any command that requires it
- `--description` for the item description (`add` command only)
- `--state` to work on Items of a different state
- `--timing` applies to the `defer` command

Sequence numbers
----------------

Sequence numbers appear in the output from the `list` command. Note that the numbering starts with 1, and is not an ID -- the number of a item will change when the collection is modified. So always reference the most recent output from the `list` command.

Sequence numbers are used with the `--criteria` option, which can be shortened to `-c`. To designate more than one item, separate the sequence numbers with a space.

Another choice is ranges. A range of sequence numbers is separated by a hyphen, with no whitespace, and is inclusive. For example, `4-6` designates items 4, 5, and 6. A hyphen without a number after it includes all the items from that item to the end of the queue. A hyphen on its own indicates the last item in the queue.

Below are some examples of task designations by sequence number.

- `busy pop -c 5` pops item number 5
- `busy drop -c 3-7` drops items 3 through 7 (4 items)
- `busy list -c 3-` lists all the items from number 3 through the end of the list
- `busy delete -c 3 5 7 9` deletes only the items designated
- `busy defer -c -` defers the last task
- `busy edit -c -4` is an error! Use `busy edit -c 1-4` instead
- `busy manage` allows you to edit the entire queue

Items will always be handled in the order they appear in the queue, regardless of the order the criteria are provided. So for example, if a `pop` command designates some items, they will be moved to the top of the queue in the order, relative to each other, they currently appear in the queue.

The sequence numbers in the `list` command output are from the collection itself. So the `list` command does not modify the sequence numbers, even when item designation is applied.

Tags
----

Items can have tags, which are space-separated hashtags in the item description. An item can have no tags, one tag, or more than one tag. For example the following item description has the tag "errands":

```
go to the supermarket #errands
```

The only punctuation that tags can contain is the hyphen ("-").

Hash tags may be used as criteria in addition to sequence numbers. For example, the following command will move all the items with the `#errands` tag to the top of the queue.

```
busy pop -c #errands
```

Whitespace-separated criteria are additive -- that is, a logical OR. For example, the following command will delete all the admin tasks, sales tasks, and tasks 3 and 4.

```
busy delete -c #admin #sales 3 4
```

_Note to self: why does this work? Shouldn't the hash symbol indicate a comment?_

Default item designations
-------------------------

For the most part, commands that accept item designations default to only act on the top item in the queue. The exceptions are:

- `list` and `manage` default to handle the entire collection
- `pop` defaults to pop the last item in the collection to the top
- `activate` defaults to activate `plan` items for today (more on that below)

Alternate queues
----------------

Busy will manage any number of queues, which are entirely separate sets of items. For example, you might have a `shopping` queue for items to buy at the store, and a `movies` queue for films you'd like to watch. The default queue is called `tasks`.

To designate an alternate queue, enter it right after the command. For example:

```
busy add shopping -d "Skimmed Milk"
busy list movies
```

Managing plans
--------------

Busy supports several specific commands related to planning -- that is, scheduling tasks for the future. They are `finish`, `defer`, and `activate`. The task-specific commands handle items in the `plan` state and, in some cases, the `done` state.

The task commands accept criteria. The `defer` and `finish` commands reference the `todo` collection; the `activate` command references the `plan` collection. The default for `defer` and `finish` is the top item in the collection; the default for `activate` is to activate only plans deferred to today or earlier.

Planning by date
----------------

Planning is by date, not time, and is relative to the current date according to the system clock.

In the `defer` command, the date can be specified using the `--timing` option. If the option is omitted, then the date can be provided as input during confirmation.

The date may take any of the following forms:

- A specific date in `YYYY-MM-DD` format, such as `2018-10-28`. Slashes are also acceptable, but the order is always year, then month, then day.
- A specific date without the year in `MM-DD` format, such as `7-4`, which will defer the item to that date in the future (even if it's in the next year).
- A specific day of the month as a simple integer, such as `12`, which will defer the item to that day of the month, in either the current month or the next month.
- An integer, a space, and the word `day` or `days`, such as `4 days`, which will defer the item to that number of days from today.
- An integer without a space and the letter `d`, such as `4d`, which is a short form of `4 days`.
- The word `tomorrow`, which is also the default if no date is provided.
- The word `today`, which is a little odd but obvious.

As an example, the following command will defer tasks 4, 5, and 6 from the `todo` collection to the date 4 days from today, keeping them in the `plan` collection until that date.

```
busy defer -c 4-6 -t "4 days"
```

Note that the `plan` collection is keeping the task information (verbatim from the `todo` collection) along with the date information (as an absolute date).

To pull tasks from the `plan` collection and put them back into the `todo` collection, use the `activate` command. There are two ways to use the `activate` command:

- With no criteria, in which case Busy activates all the tasks scheduled for today or earlier, bringing the `todo` list up to date
- With designated items from the `plan` collection; note that the `activate` command accepts item designation from the `plan` queue itself so use `busy list -s plan` first to get the right list.

Finishing and following up
--------------------------

The `finish` command removes the designated Task (or the top task if none is designated) from the `todo` state  and adds it to the `done` state, with today's date to indicate when it was completed.

Optionally, a task can have a "followon", which is another task to be added as a `todo` after the first task is finished. Followons are described in a task using an arrow notation. In the following example, the task "eat" has a followon task "drink":

```
eat --> drink
```

Note that the hyphens and whitespace are optional; really the marker that matters for delimiting a followon is the right angle bracket (">"). Also note that right angle bracket is not a valid character elsewhere in a task description.

When the `finish` command is executed on the task above, the "eat" task will be recorded as "done" and the "drink" task will be added to the top of the `todo` list.

Note that followons can be chained. For example, when the `finish` command is run on the task illustrated below, a new task "drink > be merry" will be added to the `todo` collection`. Only when that Task is finished will the "be merry" task itself appear.

```
eat > drink > be merry
```

Repeating tasks
---------------

A special type of followon is the repeat. In this case, instead of adding the next task to the top of the `todo` list, the entire current task -- including the followon itself -- is entered into the `plan` collection at some point in the future. Repeats allow for easy management of repeating tasks. Some examples follow.

- `check email --> repeat in 1 day`
- `phone mom --> repeat on sunday`
- `balance the checkbook --> repeat on 6`

The exact syntax for a Repeat is the word "repeat" followed by either "on" or "in" and a relative date phrase -- the same phrases that work with the `defer` command.

Note that the repetition itself only happens when the `finish` command is executed. The completed task (i.e. "check email") is entered in the `done` list and then the entire task (with the Repeat) is scheduled in the `plan` list for the appropriate time in the future.

Editing items
-------------

The `edit` and `manage` commands launch the user's default text editor to directly edit a task, the whole queue, or part of a queue. Note that `edit` and `manage` are identical commands except for their default criteria.

The definition of the "default text editor" depends on the OS and configuration but here's the logic:

1. Try the EDITOR environment variable
1. If that doesn't exist, try the `sensible-editor` command (Ubuntu)
1. If that doesn't exist, try the `open -W` command (OSX)

You must save changes and quit the editor to accept the change back into Busy.

The `edit` command with no criteria will edit the top item in the list, and the `manage` command with no criteria will edit the entire list. But it's also possible to designate items to be edited with both commands using criteria. The commands do their best to replace the edited items in place in the list order. So if you `edit` or `manage` a tag whose items are recently popped (at the top of the collection), then the edited items will still appear at the top. Even if you add items, they will be inserted after the last item in the edited set, not at the end of the queue. But all the items brought up in the editor will be edited. So if you remove an item in the editor, it will be deleted and the others will be moved up to take its place.

For faster daily use - the Curses UI
------------------------------------

Busy suports multiple user interfaces. The command line interface described above is the shell interface. The alternative is the curses UI, which draws an entirely new terminal in the same window.

_We get it - "curses" is a terrible name. It's a reference to the underlying technology._

In the Curses UI, commands can be triggered with single keystrokes, and only act on their default items (usually the top task). The UI always displays the current queue (which is always `tasks` for now) and the current (top) `todo` item` at the top of the screen.

To invoke the curses UI, type:

```
busy curses
```

Or it's the default so just type:

```
busy
```

Commands within the UI are shown with a single letter underlined. The underlined letter is the keystroke that will invoke the command. Use `q` to quit. When inside a command, use ctrl-C to cancel the command and return to the main menu.

Data storage
------------

Busy keeps the collections in plain text files, so if the tool doesn't do something you want, you may edit the files. The files are in a directory together, referred to as the "root". Each file is the named according to the following convention:

```
<queue>.<state>.psv
```

If a required file is missing, it will be created automatically. So typically, the root includes `tasks.todo.psv`, `tasks.plan.psv`, `tasks.done.txt`, and any number of custom queue files.

Technically, Busy data files are pipe-delimited data files, though the `todo` collections only have one field ("description") while the `plan` and `done` files have only two fields (date and description).

Busy is not a database (yet). There is no support for managing separate fields in the Busy tool itself.

The root is designated in one of the following ways, which are tried in order.

- The `--root` option on any command
- The `BUSY_ROOT` environment variable, if no `--root` option is provided
- A directory at `~/.busy`, which will be generated as needed if no `--root` option or `BUSY_ROOT` environment variable are provided,

Note that the `--root` option must come after `busy` but command-specific options (`--yes`, `--to`, `--for`, and `--queue`) must come after commands.

The following example shows the `--root` option with command-specific options on the same command line.

```
busy --root ~/.config/busy defer --t tuesday
```

Note that Busy does not support concurrency or locking in any form. If two commands are executing at the same time, they might overwrite each other. Overwriting is especially risky with the `edit` and `manage` commands, which keeps the user's editor open until they close it.

The format is designed to be simple but not idiot-proof. Experimentation might result in unintended consequences.

Development
===========

The code is intended to demonstrate some Python best practices:

- *Object-oriented* with classes and subclasses.
- *Dynamic configuration* using a unique approach we call "class families" - for example, the names of the commands are properties of the command classes, not in a big "if" statement.
- *Extensive testing* with high test coverage, guaranteed by CI.
- *Leverage the standard library* by requiring 3rd party PIP modules for development, but not for usage.

To set everything up:

- Requires Python 3.6.5 or later
- Clone the repo and CD into it
- Set up a venv if that's your thing
- `pip install -r requirements/freeze.txt`
- To run it: `python -m busy` ...

We use Visual Studio Code to build Busy, so there is a VS Code configuration file in the repository.

Then to run the test suite:

```
make test
```

Or to run test coverage:

```
make cover
```

And to check style:

```
make style
```

_Note to self: To publish a new build, use 'vernum' with 'major', 'minor', or 'patch' depending on how major the changes were since the last build. Then push. GitLab allows you to publish to PyPI via CI/CD, and only when Vernum has been run._

Command summary
===============

Below is a reference list of all commands, handy to correlate the one-letter version with the full version. The one-letter version is used in the curses UI, and is an alternative option in the shell UI. Some of the listed commands are yet to be implemented; they are listed here merely to reserve their names.

| Short | Full |
| --- | --- |
| a | add |
| c | activate |
| d | delete |
| e | edit |
| f | defer |
| l | list |
| m | manage |
| n | finish |
| o | pop |
| p | print |
| q | quit |
| r | drop |
| s | skip |
| t | tags |
| u | queues (list) |
| w | switch (queues) |
|   | curses (only in shell UI) |
