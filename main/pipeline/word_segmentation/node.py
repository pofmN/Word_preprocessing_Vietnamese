from .fwobject import FWObject

class Node:

    def __init__(self, in_condition: FWObject, in_conclusion: str, in_father_node,
                 in_except_node, in_if_not_node, in_depth: int):
        self.__condition = in_condition
        self.__conclusion = in_conclusion
        self.__father_node = in_father_node
        self.__except_node = in_except_node
        self.__if_not_node = in_if_not_node
        self.__depth = in_depth

    def set_if_not_node(self, node) -> None:
        self.__if_not_node = node

    def set_except_node(self, node) -> None:
        self.__except_node = node

    def set_father_node(self, node) -> None:
        self.__father_node = node

    def get_depth(self) -> int:
        return self.__depth

    def get_father_node(self):
        return self.__father_node

    def get_except_node(self):
        return self.__except_node

    def get_if_not_node(self):
        return self.__if_not_node

    def get_conclusion(self) -> str:
        return self.__conclusion

    def get_condition(self) -> FWObject:
        return self.__condition

    def count_nodes(self) -> int:
        count = 1
        if self.__except_node is not None:
            count += self.__except_node.count_nodes()

        if self.__if_not_node is not None:
            count += self.__if_not_node.count_nodes()

        return count

    def satisfy(self, ob: FWObject) -> bool:
        check: bool = True
        for i in range(0, 10):
            key: str = self.__condition.context[i]
            if key is not None:
                if not key == ob.context[i]:
                    check = False
                    break

        return check
