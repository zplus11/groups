from groups.group import G


class Map:
    def __init__(self, G1, G2, defn):
        """Defines a map from G1 to G2."""

        assert isinstance(G1, G), f"{G1} is not a group."
        assert isinstance(G2, G), f"{G2} is not a group."
        assert callable(defn), f"Function is not callable."

        for x in G1:
            assert defn(x) in G2, f"Invalid map, images going out of codomain."
        
        self.domain = G1
        self.codomain = G2
        self.image = defn
        self.map = {x: self.image(x) for x in self.domain}

    def __repr__(self):
        """Represents the map."""

        return f"𝜙: {repr(self.domain)} --> {repr(self.codomain)}"

    def __call__(self, x):
        """Calls the map on x."""

        return self.image(x)

    def one_one(self):
        """Checks if the map is one-one."""

        return len(self.domain) == len(set(self.map.values()))

    def op(self):
        """Checks if the map is order preserving."""

        if any(self.image(self.domain.apply(x, y)) != self.codomain.apply(self.image(x), self.image(y)) \
               for x in self.domain for y in self.domain):
            return False
        return True

class Homomorphism(Map):
    def __init__(self, G1, G2, defn):
        """Defines a Homomorphism from a group G1 to G2."""

        super().__init__(G1, G2, defn)
        assert self.op(), f"The map is not operation preserving."

    def kernal(self):
        """"Returns the kernal of this homomorphism."""

        return {x for x in self.domain if self.image(x) == self.codomain.identity}

class Isomorphism(Map):
    def __init__(self, G1, G2, defn):
        """Defines an Isomorphism from a group G1 to G2."""

        super().__init__(G1, G2, defn)
        assert self.op(), f"The map is not operation preserving."
        assert self.one_one(), f"The map is not one-one."

class Automorphism(Isomorphism):
    def __init__(self, G, defn):
        """Defines an Automorphism from G onto itself."""

        super().__init__(G, G, defn)

class IAutomorphism(Automorphism):
    def __init__(self, G1, a):
        """Defines the inner Automorphism of G induced by a."""

        assert isinstance(G1, G), f"Invalid group {G1}"
        assert a in G1, f"Invalid member {a}"
        super().__init__(G1, lambda x: G1.apply(a, x, G1.inverse(a)))
