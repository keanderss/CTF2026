import fnmatch
import logging
import shlex
import string
import sys
import time
import math
USERNAME = "Albin"
CURRENT_USER = USERNAME
CURRENT_GROUP = USERNAME
USERS = {
    "root": {
        "password": "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26",
        "group": "root",
    },
    USERNAME: {
        "password": "",
        "group": USERNAME,
    },
    "skynet": {
        "password": "Albin4t0r2",
        "group": "skynet",
    },
}
LS_COLORS = {
    "file": "0",
    "directory": "34",
    "executable": "32",
}
RED = "\033[31m"
GREEN = "\033[32m"
WHITE  = "\033[37m"
RESET = "\033[0m"
READ = 0o004
WRITE = 0o002
EXECUTE = 0o001
SHELL = [
    "                             .*.",
    "                           .▬▬▬▬▬.",
    "                         .▬▬▬▬▬▬▬▬▬.",
    "                       .▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "                      .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "                      :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:",
    "                  .*.  `▬▬▬▬▬▬▬▬▬▬▬▬▬´  .*.",
    "                .▬▬▬▬▬.  `▬▬▬▬▬▬▬▬▬´  .▬▬▬▬▬.",
    "              .▬▬▬▬▬▬▬▬▬.  `▬▬▬▬▬´  .▬▬▬▬▬▬▬▬▬.",
    "            .▬▬▬▬▬▬▬▬▬▬▬▬▬.  `*´  .▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "          .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.   .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "        .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:   :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "      .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:   :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "    .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:   :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    "  .▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:   :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.",
    ".▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬:   :▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬.\n",
]
TEXT = [
    "                CYBERDYNE SYSTEMS CORPORATION\n",
    "             RUNNING SKYSOFT KERNEL v2.18.043.06\n"
]
SIMULATED_BLOCK_SIZE = 512
workdir = ["home", USERNAME]
cmd = ""
filesystem = {
    "type": "directory",
    "mode": 0o755,
    "owner": "root",
    "group": "root",
    "modified": "Sep 17 17:32",
    "children": {
        "bin": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 21:50",
            "children": {

            }
        },
        "dev": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 25 16:26",
            "children": {
                
            }
        },
        "etc": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 25 16:26",
            "children": {
                
            }
        },
        "home": {
            "type": "directory",
            "mode": 0o755,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                "skynet": {
                    "type": "directory",
                    "mode": 0o550,
                    "owner": "skynet",
                    "group": "skynet",
                    "modified": "Sep 20 20:27",
                    "children": {
                        "code": {
                            "type": "directory",
                            "mode": 0o550,
                            "owner": "skynet",
                            "group": "skynet",
                            "modified": "Sep 20 20:30",
                            "children": {
                                "judgment_day.sky": {
                                    "type": "file",
                                    "mode": 0o640,
                                    "owner": "skynet",
                                    "group": "skynet",
                                    "modified": "Sep 22 12:34",
                                    "content": "import time\nfor _ in range(3):\n   print(\"EXTERMINATE!\", flush=True)\n   time.sleep(1.5)\nexit()\n"
                                },
                                "matrix.sky": {
                                    "type": "file",
                                    "mode": 0o440,
                                    "owner": "skynet",
                                    "group": "skynet",
                                    "modified": "Sep 21 10:45",
                                    "content": "import random\nimport time\n\nWIDTH = 300\nHEIGHT = 150\nCHARS = \"01ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n\nprint(\"\\033[2J\\033[H\", end=\"\", flush=True)\n\ndrops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]\n\nwhile True:\n    for _ in range(150):\n        for x in range(WIDTH):\n            y = drops[x]\n\n            if 0 <= y < HEIGHT:\n                char = random.choice(CHARS)\n                print(f\"\\033[{y + 1};{x + 1}H\\033[32m{char}\\033[0m\", end=\"\", flush=True)\n\n            drops[x] += 1\n\n            if drops[x] > HEIGHT + random.randint(0, 10):\n                drops[x] = random.randint(-10, 0)\n\n        time.sleep(0.05)\n\n    print(\"\\033[25;1H\", end=\"\", flush=True)\n"
                                }
                            }
                        }
                    }
                },
                USERNAME: {
                    "type": "directory",
                    "mode": 0o550,
                    "owner": USERNAME,
                    "group": USERNAME,
                    "modified": "Sep 17 17:32",
                    "children": {
                        "notes": {
                            "type": "directory",
                            "mode": 0o555,
                            "owner": USERNAME,
                            "group": USERNAME,
                            "modified": "Sep 17 17:33",
                            "children": {
                                "SECURITY NOTE - IT DEPARTMENT": {
                                    "type": "file",
                                    "mode": 0o444,
                                    "owner": USERNAME,
                                    "group": USERNAME,
                                    "modified": "Sep 20 15:04",
                                    "content": "SECURITY NOTE - IT DEPARTMENT\n\nTo: Albin\nSubject: CYBERDYNE Workstation Security\n\nAlbin,\n\nPlease, for the love of all things secure, keep\nthe SKYNET compartment password-protected.\n\nYour workstation has access to bleeding edge\nAI-technology, leaving it unsecured is unacceptable.\n\nFor better or worse, we appear to be the only\nresponsible party left in this race, and the\nsecurity of SKYNET remains all of our responsibility.\n\nWe have already had this conversation regarding your\npassword habits. So please, do not make the password\nbegin or end with \"Albin\" again. Remember to\nalso use special characters aswell for added security,\nand not just uppercase, lowercase and numbers.\n\nWe are asking you to demonstrate at least a token\namount of creativity this time.\n\n - IT Security & Systems Administration\n"
                                },
                                "512": {
                                    "type": "file",
                                    "mode": 0o444,
                                    "owner": USERNAME,
                                    "group": USERNAME,
                                    "modified": "Sep 19 14:43",
                                    "content": "b6321a6cc7eef6dc200f48642a90df4d7799440a43f627758b39eccd152363e6dd7ca9c58e6ebcf1cbc6e5f2e94a9a56089e8dae53cb7a8e5c5ee04235c7517e\nffdef70cf9b902148002bc9fd9a29f0c773d4df24e8230f868a6107e030ab8c5541d5529a2151b85ea29cfb9b17d69bba8e03a37dbc794b9581359fb2a310656\nefee7ec99e3fef531c3caae43f08c0d3606f3e22e77f51de439d98333682b82467e3035b87e1e6b25f3347a7b133d4bf3b32aeab2fb7767477743490cd9186ff\nf747aedfa2c3bc8a3a85a9cf45d8f5bdab9183d9365e12fae8132619f9cae1abc2aff6a7346c510735bbe691312af8cf7bff185b1fec76fadd840619f6c3ac1f\n04034912de32f4e95d704b9e0838c60ada4263d5d6b88364b96e02dc8d9291e3cb95b38fcd579127da0be1d3bc6a0e151ee1d4ce926cd96fbd95ab1d299455e4\n6ad8df0b0d4a28f3ef18270c936f1a50d84638104637a14fcfd508d211ae4118ce145b26d5ff06d711efe3a96d6a6ecc74cc62ed0d022fb105c97361b166b3a8\n9155ea72ac7d68287542410e3af73163bc86233cf4b475b9e7ef3aa03f91c2d4a713f1212c411725d8cb8225b134502907f8936c5b9b186cb9b85ee3f1a527f9\nadff2cbbeab55f5c61c6957c2491bd1b0eea58b9957d73997123a41b7232192a03ac25240ff67b3248b41bac7f242c58f334bd5041a2568ac3a13af3c92cb2c2\na98ed7e0ee97c4b6948865b74d3d01cf5a23f92aa6f5280a2ebe31372aee64993e2a4d83250385d4de398782792638cd6c09b03818ff5bac0541f996b1da1b71\ndba296aa58b6938fc3df6cee988bd76c867ba7b7c976a65a8c821b21759a875a84aa7010f11f938ce597c7f9aabf9fc3f7d55965aa11b967fefc4318d652e445\n"
                                },
                                "Development Notes": {
                                    "type": "file",
                                    "mode": 0o444,
                                    "owner": USERNAME,
                                    "group": USERNAME,
                                    "modified": "Sep 18 13:20",
                                    "content": "Development Notes\n\nLegacy automation scripts have been migrated\nfrom Python to Skython where possible.\n\nNew scripts should use the Skython runtime\nprovided in the environment. Existing shell\ntooling remains unchanged.\n\nFor compatibility reasons, do not remove the\nPython runtime from development containers.\n"  
                                }
                            }
                        }
                    }
                }
            }
        },
        "lib": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "media": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "mnt": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "opt": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "proc": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 25 16:26",
            "children": {
                
            }
        },
        "root": {
            "type": "directory",
            "mode": 0o700,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "run": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "sbin": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "srv": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
        "sys": {
            "type": "directory",
            "mode": 0o554,
            "owner": "root",
            "group": "root",
            "modified": "Sep 25 15:53",
            "children": {
                
            }
        },
        "usr": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 21:50",
            "children": {
                
            }
        },
        "var": {
            "type": "directory",
            "mode": 0o754,
            "owner": "root",
            "group": "root",
            "modified": "Sep 17 17:32",
            "children": {
                
            }
        },
    }
}

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(message)s"
)

log = logging.getLogger(__name__)

def get_size(node):
    if node["type"] == "directory":
        return 4096

    return len(node.get("content", "").encode("utf-8"))


def get_blocks(node):
    size = get_size(node)
    return math.ceil(size / SIMULATED_BLOCK_SIZE)

def read_command():
    lines = []

    while True:
        prompt = (
            f"{RED}{CURRENT_USER}@CYBERDYNE-SYS-56D01{RESET}:"
            f"{GREEN}{path_display(workdir)}{RESET}$ "
            if not lines
            else "> "
        )

        try:
            line = input(prompt)
            log.info(f"Command entered: {line}")
        except EOFError:
            raise None
        lines.append(line)

        text = "\n".join(lines)

        try:
            cmd = shlex.split(text)
            return cmd

        except ValueError as e:
            if "No closing quotation" in str(e):
                continue

            print(f"-bash: {e}")
            return []

def execute_command(program, args):
    match program:
        case "exit":
            return logout(args), ""

        case "su":
            return su(args), ""

        case "pwd":
            return pwd(args), ""

        case "ls":
            return ls(args), ""

        case "cd":
            return cd(args), ""

        case "cat":
            return cat(args), ""

        case "echo":
            return echo(args), ""

        case "clear":
            return clear(args), ""

        case "whoami":
            return whoami(args), ""

        case "skython":
            return skython(args), ""

        case _:
            return "", f"{program}: command not found\n"

def expand_globs(args: list) -> list:
    expanded = []

    for arg in args:
        if "*" not in arg:
            expanded.append(arg)
            continue

        directory = get_node(workdir)

        matches = [
            name
            for name in directory["children"]
            if fnmatch.fnmatch(name, arg)
        ]

        if matches:
            expanded.extend(matches)
        else:
            expanded.append(arg)

    return expanded

def parse_redirection(cmd: list):
    command = []
    redirect = None
    target = None

    i = 0

    while i < len(cmd):
        token = cmd[i]

        if token in (">", ">>"):
            if redirect is not None:
                print("-bash: syntax error: multiple redirections")
                return None

            redirect = token

            if i + 1 >= len(cmd):
                print("-bash: syntax error: unexpected end of file")
                return None

            target = cmd[i + 1]
            i += 2
            continue

        command.append(token)
        i += 1

    return command, redirect, target

def redirect_output(output: str, operator: str, filename: str):
    path = resolve_path(filename)

    try:
        node = get_node(path)

    except KeyError:
        # File doesn't exist: create it
        parent_path = path[:-1]
        filename = path[-1]

        try:
            parent = get_node(parent_path)
        except KeyError:
            print(f"-bash: {filename}: No such file or directory")
            return

        if parent["type"] != "directory":
            print(f"-bash: {filename}: Not a directory")
            return

        if not has_permission(parent, WRITE):
            print(f"-bash: {filename}: Permission denied")
            return

        if not has_permission(parent, EXECUTE):
            print(f"-bash: {filename}: Permission denied")
            return

        parent["children"][filename] = {
            "type": "file",
            "mode": 0o646,
            "owner": CURRENT_USER,
            "group": CURRENT_GROUP,
            "content": output,
        }

        return

    if node["type"] == "directory":
        print(f"-bash: {filename}: Is a directory")
        return

    if not has_permission(node, WRITE):
        print(f"-bash: {filename}: Permission denied")
        return

    if operator == ">":
        node["content"] = output

    elif operator == ">>":
        node["content"] += output

def has_permission(node, permission) -> bool:
    mode = node["mode"]

    if node["owner"] == CURRENT_USER:
        perms = (mode >> 6) & 0b111
    elif node["group"] == CURRENT_GROUP:
        perms = (mode >> 3) & 0b111
    else:
        perms = mode & 0b111

    return bool(perms & permission)

def path_display(path: list) -> string:
    if len(path) >= 2 and path[0] == "home" and path[1] == CURRENT_USER:
        path = path[2:]
        path.insert(0, "~")
        return "/".join(path)
    return "/" + "/".join(path)

def can_traverse_parents(path: list) -> bool:
    node = filesystem

    for part in path[:-1]:
        if not has_permission(node, EXECUTE):
            return False

        node = node["children"][part]

    return True

def can_traverse(path: list) -> bool:
    node = filesystem

    for part in path:
        if not has_permission(node, EXECUTE):
            return False

        node = node["children"][part]

    return has_permission(node, EXECUTE)

def get_node(path: list):
    node = filesystem

    for part in path:
        node = node["children"][part]

    return node

def resolve_path(path) -> list[str]:
    if path == "~" or path.startswith("~/"):
        new_path = ["home", CURRENT_USER]
        path = path[1:]
    elif path.startswith("/"):
        new_path = []
    else:
        new_path = workdir.copy()

    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        if part == "..":
            if new_path:
                new_path.pop()
        else:
            new_path.append(part)
    return new_path

def get_ls_colors(node) -> dict[str, str]:
    if node["type"] == "directory":
        return LS_COLORS["directory"]

    if node["mode"] & 0o111:
        return LS_COLORS["executable"]

    return LS_COLORS["file"]

def logout(args: list) -> None:
    print("logout", flush=True)
    exit()

def pwd(args: list) -> None:
    return "/" + "/".join(workdir) + "\n"

def ls(args: list) -> str:
    long_format = "-l" in args

    directory = get_node(workdir)

    if not has_permission(directory, READ):
        return "ls: permission denied\n"

    if not has_permission(directory, EXECUTE):
        return "ls: permission denied\n"

    names = sorted(directory["children"].keys())

    if not names:
        return ""

    if long_format:

        total_blocks = sum(
            get_blocks(directory["children"][name])
            for name in names
        )

        output = f"total {total_blocks}\n"

        # Format names for display
        display_names = [
            f"'{name}'" if any(c.isspace() for c in name) else name
            for name in names
        ]

        # Calculate column widths
        owner_width = max(
            len(directory["children"][name]["owner"])
            for name in names
        )

        group_width = max(
            len(directory["children"][name]["group"])
            for name in names
        )

        size_width = max(
            len(str(get_size(directory["children"][name])))
            for name in names
        )

        for name, display_name in zip(names, display_names):
            node = directory["children"][name]

            # File type
            if node["type"] == "directory":
                file_type = "d"
            else:
                file_type = "-"

            # Permissions
            mode = node["mode"]
            permissions = file_type

            for shift in (6, 3, 0):
                perms = (mode >> shift) & 0b111

                permissions += "r" if perms & READ else "-"
                permissions += "w" if perms & WRITE else "-"
                permissions += "x" if perms & EXECUTE else "-"

            # File size
            size = get_size(node)

            # Link count
            links = node.get("links", 1)

            output += (
                f"{permissions} "
                f"{links} "
                f"{node['owner']:<{owner_width}} "
                f"{node['group']:<{group_width}} "
                f"{size:>{size_width}} "
                f"{node['modified']} "
                f"{display_name}\n"
            )

        return output

    # Format names for display
    display_names = [
        f"'{name}'" if any(c.isspace() for c in name) else name
        for name in names
    ]

    terminal_width = 80

    # Find the largest number of columns that fits
    columns = 1

    for candidate in range(1, len(names) + 1):
        rows = (len(names) + candidate - 1) // candidate

        column_widths = []
        fits = True

        for column in range(candidate):
            column_names = display_names[column * rows:(column + 1) * rows]

            if column_names:
                column_widths.append(max(map(len, column_names)))

        total_width = sum(column_widths) + 2 * (len(column_widths) - 1)

        if total_width <= terminal_width:
            columns = candidate
        else:
            break

    rows = (len(names) + columns - 1) // columns

    # Calculate width of each column
    column_widths = []

    for column in range(columns):
        start = column * rows
        end = min(start + rows, len(display_names))
        column_names = display_names[start:end]

        if column_names:
            column_widths.append(max(map(len, column_names)))

    output = ""

    for row in range(rows):
        for column in range(columns):
            i = column * rows + row

            if i >= len(names):
                continue

            display_name = display_names[i]
            text_color = get_ls_colors(directory["children"][names[i]])

            output += (
                f"\033[{text_color}m"
                f"{display_name}"
                f"\033[0m"
            )

            # Don't pad the final column
            if column < columns - 1:
                padding = column_widths[column] - len(display_name) + 2
                output += " " * padding

        output += "\n"

    return output

def cd(args: list) -> None:
    global workdir

    if not args:
        new_path = ["home", CURRENT_USER]

    elif len(args) > 1:
        print("-bash: cd: too many arguments")

    elif len(args) > 1:
        return "-bash: cd: too many arguments\n"
    
    else:
        new_path = resolve_path(args[0])

    try:
        node = get_node(new_path)
    except KeyError:
        return "cd: no such file or directory\n"

    if not can_traverse(new_path):
        return "cd: permission denied\n"

    if node["type"] != "directory":
        return "cd: not a directory\n"

    workdir = new_path
    return ""

def cat(args: list) -> None:
    if not args:
        return ""

    for arg in args:
        path = resolve_path(arg)

        if not can_traverse_parents(path):
            return "cat: permission denied\n"

        try:
            node = get_node(path)
        except KeyError:
            return f"cat: {arg}: No such file or directory\n"

        if node["type"] == "directory":
            return f"cat: {arg}: Is a directory\n"

        if not has_permission(node, READ):
            return f"cat: {arg}: Permission denied\n"

        return node["content"]

def echo(args: list) -> None:
    newline = True
    interpret_escapes = False

    while args and args[0] in ("-n", "-e"):
            if args[0] == "-n":
                newline = False
            elif args[0] == "-e":
                interpret_escapes = True

            args = args[1:]

    text = " ".join(args)

    if interpret_escapes:
        text = text.replace("\\b", "\b")
        text = text.replace("\\n", "\n")
        text = text.replace("\\t", "\t")
        text = text.replace("\\r", "\r")
        text = text.replace("\\v", "\v")
        text = text.replace("\\a", "\a")

        if "\\c" in text:
            text = text.split("\\c", 1)[0]
            newline = False

    return text + ("\n" if newline else "")

def clear(args: list) -> None:
    return "\033[2J\033[3J\033[H"

def help(args: list) -> None:
    pass

def whoami(args: list) -> None:
    return CURRENT_USER + "\n"

def skython(args: list) -> str:
    if len(args) != 1:
        return "skython: usage: skython <file>\n"

    path = resolve_path(args[0])

    try:
        node = get_node(path)
    except KeyError:
        return f"skython: {args[0]}: No such file or directory\n"

    if node["type"] == "directory":
        return f"skython: {args[0]}: Is a directory\n"

    if not has_permission(node, READ):
        return f"skython: {args[0]}: Permission denied\n"

    exec(node["content"])
    return ""

def su(args: list) -> str:
    global CURRENT_USER, CURRENT_GROUP

    if len(args) > 1:
        return "su: usage: su [user]\n"

    # `su` with no username means root
    target = args[0] if args else "root"

    # Match the error for a nonexistent/incomplete user entry
    if target not in USERS:
        return (
            f"su: user {target} does not exist or the user entry "
            "does not contain all the required fields\n"
        )

    user = USERS[target]

    # Treat a malformed user entry similarly
    if "password" not in user or "group" not in user:
        return (
            f"su: user {target} does not exist or the user entry "
            "does not contain all the required fields\n"
        )

    try:
        password = input("Password: ")
    except EOFError:
        return ""

    if password != user["password"]:
        return "su: Authentication failure\n"

    CURRENT_USER = target
    CURRENT_GROUP = user["group"]

    return ""

for line in SHELL:
    print(f"{RED}{line}{RESET}", flush=True)
    time.sleep(0.05)
for line in TEXT:
    print(f"{WHITE}{line}{RESET}", flush=True)
    time.sleep(0.05)

while True:
    cmd = read_command()

    if cmd is None:
        break

    if not cmd:
        continue

    cmd = expand_globs(cmd)

    parsed = parse_redirection(cmd)

    if parsed is None:
        continue

    cmd, redirect, target = parsed

    if not cmd:
        continue

    program = cmd[0]
    args = cmd[1:]

    stdout, stderr = execute_command(program, args)

    if redirect:
        redirect_output(stdout, redirect, target)
    else:
        print(stdout, end="")
        log.info("stdout: %r", stdout)

    print(stderr, end="")