import numpy as np

from chromatic_tda.utils.persistence_utils import PersistenceUtils


class CoreSimplicialComplex():

    dim_simplex_dict : dict[int, set]
    simplex_weights : dict[tuple, float]
    boundary : dict[tuple, set]
    co_boundary : dict[tuple, set]
    sub_complex : set
    persistence_data : dict
    birth_death : dict

    def __init__(self) -> None:
        # should we just call clear?
        self.dim_simplex_dict = {}     # self.dim
        self.simplex_weights = {}  # self.rad

        self.boundary = {}      # example: {(1,2,3) : {(1,2), (1,3), (2,3)}, (1,2) : {(1), (2)}, ...}  
        self.co_boundary = {}   # example:  {(1,2) : {(1,2,3), (1,2,4)}, (1,3) : {(1,2,3), (1,3,4)}, ...}

        self.sub_complex = set()
        self.persistence_data = {}
        self.birth_death = {}

        self.dimension : int
        
    def clear(self) -> None:
        self.dim_simplex_dict = {}
        self.simplex_weights = {}
        
        self.boundary = {}
        self.co_boundary = {}

        self.sub_complex = set()
        self.persistence_data = {}
        self.birth_death = {}

    def clear_empty_dimensions(self) -> None:
        clear_dims = []
        for dim in self.dim_simplex_dict:
            if len(self.dim_simplex_dict[dim]) == 0:
                clear_dims.append(dim)
        for dim in clear_dims:
            self.dim_simplex_dict.pop(dim)

    def __len__(self) -> int:
        return len(self.boundary)

    def __contains__(self, item) -> bool:
        return item in self.boundary

    def set_simplex_weighs(self, radius_function, default_value = 0) -> None:
        """
        Add radii of simplices from a dictionary `simplex : radius`.
        Add default_value to all simplices not present in the radius function.

        Note: Monotonicity is NOT checked.
        """
        self.simplex_weights = {simplex : default_value for simplex in self.boundary}
        for simplex,radius in radius_function.items():
            self.simplex_weights[tuple(sorted(simplex))] = radius

    def get_bars_list(self, group, dim = None, only_finite = False) -> list:
        """
        Return list of pairs representing bars of a given dimension.
        If `dim` is not given, returns all bars in form `(dim, (birth, death))`.
        The groups to choose from (`group`) are:
            complex, sub_complex, image, kernel, cokernel, relative
        """
        if self.birth_death is None:
            raise ValueError("Persistence not yet computed, run `compute_persistence` first.")
        if group not in self.birth_death:
            raise ValueError(f"Persistence for `{group}` not computed. Did you run `compute_persistence`?")
        
        dim_bars_finite : list[tuple[int, tuple[float, float]]] = [
            (len(s)-1 if group != 'kernel' else len(s)-2,
            (self.simplex_weights[s], self.simplex_weights[t])) for s, t in self.birth_death[group]['pairs']
        ]
        if only_finite:
            dim_bars_infinite = []
        else:
            dim_bars_infinite : list[tuple[int, tuple[float, float]]] = [
                (len(s)-1 if group != 'kernel' else len(s)-2,
                (self.simplex_weights[s], np.inf)) for s in self.birth_death[group]['essential']
            ]
        dim_bars = dim_bars_finite + dim_bars_infinite

        if dim is None:
            return sorted([b for b in dim_bars if not PersistenceUtils().is_trivial_bar(b[1])])
        else:
            bars : list[tuple] = [bar for bar_dim, bar in dim_bars if bar_dim == dim]
            return sorted([b for b in bars if not PersistenceUtils().is_trivial_bar(b)])

    def get_simplices(self) -> list:
        """Return list of all simplices sorted by dimension and then lexicographically."""
        return sorted(self.boundary, key=lambda s: (len(s),s))

    def get_simplices_of_dim(self, dim) -> list:
        return sorted(self.dim_simplex_dict[dim])

    def get_simplices_of_dim_count(self, dim) -> int:
        return len(self.dim_simplex_dict[dim])

    def get_sub_complex_simplices(self) -> list:
        """Return list of all simplices of the sub_complex, sorted by dimension and then lexicographically."""
        return sorted(self.sub_complex, key=lambda s: (len(s), s))

    def get_vertices(self) -> list:
        """Return list of all vertices."""
        return sorted(v[0] for v in self.dim_simplex_dict[0])

    def set_simplex_weights(self, radius_function, default_value = 0) -> None:
        """
        Add radii of simplices from a dictionary `simplex : radius`.
        Add default_value to all simplices not present in the radius function.

        Note: Monotonicity is NOT checked.
        """
        # set_radii function
        self.simplex_weights = {simplex : default_value for simplex in self.boundary}
        for simplex,weight in radius_function.items():
            self.simplex_weights[tuple(sorted(simplex))] = weight

    def set_sub_complex(self, simplices) -> None:
        """Sets a sub_complex generated by given list of simplices."""
        simplices = set(tuple(sorted(s)) for s in simplices)
        queue = sorted(simplices, key=lambda s:(len(s),s))
        while queue:
            simplex = queue.pop()
            simplex_boundary = self.boundary[simplex]
            for sub_simplex in simplex_boundary:
                if sub_simplex not in simplices:
                    simplices.add(sub_simplex)
                    queue.append(sub_simplex)
        self.sub_complex = simplices

    def set_total_sub_complex(self, vertices) -> None:
        """Sets a sub_complex as the total sub_complex given by a list of vertices."""
        vertices = set(vertices)
        self.sub_complex = set(s for s in self.boundary if set(s).issubset(vertices))

    def get_dimension(self) -> int:
        return len(self.dim_simplex_dict)-1

    def write(self) -> None:
        print()
        print(f"*** Simplicial Complex (dimension = {self.get_dimension()})")
        for dim in range(0, self.get_dimension()+1):
            print(f"Simplices with dimension {dim} ({self.get_simplices_of_dim_count(dim)}): {self.get_simplices_of_dim(dim)}")
