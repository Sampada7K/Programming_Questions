class Graph:
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict
        self.project_state = {}
        for project in self.get_projects():
            self.project_state[project] = "Blank"

    def get_projects(self):
        return list(self.graph_dict.keys())

    def get_dependencies(self, project):
        if project and project in self.graph_dict:
            return self.graph_dict[project]

    def get_project_state(self, project):
        if project and project in self.project_state:
            return self.project_state[project]

    def set_project_state(self, project, state):
        if project and project in self.graph_dict:
            if state and state in {"Partial", "Complete"}:
                self.project_state[project] = state


def find_build_order(graph: Graph):
    build_order = []
    for project in graph.get_projects():
        if graph.get_project_state(project) is "Blank":
            if not find_build_order_util(graph, project, build_order):
                return None

    return build_order


def find_build_order_util(graph, project, build_order):
    print(graph.project_state)
    if graph.get_project_state(project) is "Partial":
        # Cycle Detected
        print(f"Cycle detected for project {project}")
        return False
    if graph.get_project_state(project) is "Blank":
        graph.set_project_state(project, "Partial")
        dependencies = graph.get_dependencies(project)
        for dependency in dependencies:
            if not find_build_order_util(graph, dependency, build_order):
                # Cycle Detected
                print(f"Cycle detected for project {project}")
                return False

        graph.set_project_state(project, "Complete")
        build_order.append(project)
    return True


def find_build_order_mine(graph: Graph):
    build_order = []
    for project in graph.get_projects():
        if graph.get_project_state(project) is "Blank":
            if not find_build_order_util_mine(graph, project, build_order):
                return None

    return build_order


def find_build_order_util_mine(graph: Graph, project, build_order):
    print(graph.project_state)
    if graph.get_project_state(project) is "Partial":
        # Cycle Detected
        print(f"Cycle detected for project {project}")
        return False
    graph.set_project_state(project, "Partial")
    dependencies = graph.get_dependencies(project)
    for dependency in dependencies:
        if graph.get_project_state(dependency) is "Partial":
            # Cycle Detected
            print(f"Cycle detected for project {dependency}")
            return False
        if graph.get_project_state(dependency) is "Blank":
            find_build_order_util_mine(graph, dependency, build_order)

    graph.set_project_state(project, "Complete")
    build_order.append(project)
    return True


graph_dict1 = {"a": ["f", "e"],
               "b": ["f"],
               "c": ["e"],
               "d": ["a", "b", "c"],
               "e": [],
               "f": [],
               }

graph1 = Graph(graph_dict1)

project_build_order = find_build_order(graph1)
if project_build_order:
    print(f"CTCI {project_build_order}")
else:
    print("Graph has a cycle, no valid build order.")




graph_dict1 = {"a": ["f", "e"],
               "b": ["f"],
               "c": ["e"],
               "d": ["a", "b", "c"],
               "e": [],
               "f": [],
               }

graph1 = Graph(graph_dict1)

project_build_order_mine = find_build_order_mine(graph1)
if project_build_order_mine:
    print(f"Mine {project_build_order_mine}")
else:
    print("Graph has a cycle, no valid build order.")