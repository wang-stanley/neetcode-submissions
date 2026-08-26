class Solution:
    def simplifyPath(self, path: str) -> str:
        splitPath = path.split("/")
        print(f"Split Path: {splitPath}")

        stack = []

        for token in splitPath:
            match token:
                case "":
                    continue
                case ".":
                    continue
                case "..":
                    if stack:
                        stack.pop()
                case _:
                    stack.append(token)

        return "/" + "/".join(stack)