from os.path import exists

TOP_ENUM = "use std::str::FromStr;\n\npub enum %name% {\n"
BOT_ENUM = "}\n\n"

TOP_FROM = "impl FromStr for %name% {\n\ttype Err = ();\n\tfn from_str(input: &str) -> Result<%name%, Self::Err> {\n\t\tmatch input {\n"
BOT_FROM = "_ => Err(()),\n}\n}\n}"

TOP_NAME = "impl %name% {\n\tpub fn name(&self) -> String { \n\t\tmatch *self {\n"
BOT_NAME = "\t\t}\n\t}\n}"


def get_input():
    if not exists("input.txt"):
        print("input.txt doesn't exist")
        return None
    with open('input.txt', 'r+') as file:
        return [e.strip().split(":") for e in file.readlines()]


def main():
    print("Name for enum: ")
    name = input()
    if name == "":
        return
    lines = []
    lines.append(TOP_ENUM.replace("%name%", name))
    input_lines = get_input()
    if input_lines is None:
        return
    for e in input_lines:
        lines.append("\t" + e[0] + ",\n")
    lines.append(BOT_ENUM)
    lines.append("")
    lines.append(TOP_FROM.replace("%name%", name))
    for e in input_lines:
        lines.append("\t\t\t\"" + e[0] + "\"" + " => " + name + "::" + e[0] + "\n")
    lines.append(BOT_FROM)
    lines.append("")
    lines.append(TOP_NAME.replace("%name%", name))
    for e in input_lines:
        lines.append("\t\t\t" + name + "::" + e[0] + " => \"" + e[1] + "\".to_string(),\n")
    lines.append(BOT_NAME)
    with open('output.rs', 'w+') as file:
        file.writelines(lines)


if __name__ == '__main__':
    main()
