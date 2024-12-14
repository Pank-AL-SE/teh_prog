class TMember:
    def __init__(self, coeff=0, degree=0):
        self.FCoeff = coeff
        self.FDegree = degree

    def get_coeff(self):
        return self.FCoeff

    def set_coeff(self, coeff):
        self.FCoeff = coeff

    def get_degree(self):
        return self.FDegree

    def set_degree(self, degree):
        self.FDegree = degree

    def is_equal(self, other):
        return self.FCoeff == other.FCoeff and self.FDegree == other.FDegree

    def differentiate(self):
        if self.FDegree == 0:
            return TMember(0, 0)
        return TMember(self.FCoeff * self.FDegree, self.FDegree - 1)

    def evaluate(self, x):
        return self.FCoeff * (x ** self.FDegree)

    def to_string(self):
        if self.FCoeff == 0 or self.FDegree < 0:
            return "0"
        result = ""
        if self.FCoeff != 1 or self.FDegree == 0:
            result += str(self.FCoeff)
        if self.FDegree > 0:
            result += "x"
            if self.FDegree > 1:
                result += "^" + str(self.FDegree)
        return result

    def __eq__(self, other):
        return self.FCoeff == other.FCoeff and self.FDegree == other.FDegree

    def __repr__(self):
        return f"TMember({self.FCoeff}, {self.FDegree})"


class TPoly:
    def __init__(self, members=None):
        # Если members не передан, создаем пустой список
        if members is None:
            self.members = []
        else:
            self.members = members

    @property
    def degree(self):
        if not self.members:
            return -1
        return max(member.get_degree() for member in self.members)

    def coefficient(self, n):
        for member in self.members:
            if member.get_degree() == n:
                return member.get_coeff()
        return 0

    def clear(self):
        self.members.clear()

    def add(self, other):
        result = TPoly()
        all_members = self.members + other.members
        
        # Объединяем члены с одинаковыми степенями
        unique_degrees = {member.get_degree() for member in all_members}
        for degree in sorted(unique_degrees, reverse=True):
            total_coeff = sum(member.get_coeff() for member in all_members if member.get_degree() == degree)
            if total_coeff != 0:
                result.members.append(TMember(total_coeff, degree))
                
        return result

    def multiply(self, other):
        result = TPoly()
        for m1 in self.members:
            for m2 in other.members:
                new_member = TMember(m1.get_coeff() * m2.get_coeff(), m1.get_degree() + m2.get_degree())
                result.members.append(new_member)

        # Упрощаем результат, объединяя члены с одинаковыми степенями
        unique_degrees = {member.get_degree() for member in result.members}
        simplified_members = []
        for degree in sorted(unique_degrees, reverse=True):
            total_coeff = sum(member.get_coeff() for member in result.members if member.get_degree() == degree)
            if total_coeff != 0:
                simplified_members.append(TMember(total_coeff, degree))
        result.members = simplified_members
        return result

    def subtract(self, other):
        result = TPoly()
        for m1 in self.members:
            result.members.append(m1)
        for m2 in other.members:
            result.members.append(TMember(-m2.get_coeff(), m2.get_degree()))

        # Упрощаем результат, объединяя члены с одинаковыми степенями
        unique_degrees = {member.get_degree() for member in result.members}
        simplified_members = []
        for degree in sorted(unique_degrees, reverse=True):
            total_coeff = sum(member.get_coeff() for member in result.members if member.get_degree() == degree)
            if total_coeff != 0:
                simplified_members.append(TMember(total_coeff, degree))
        result.members = simplified_members
        return result

    def negate(self):
        result = TPoly()
        for member in self.members:
            result.members.append(TMember(-member.get_coeff(), member.get_degree()))
        return result

    def equals(self, other):
        return sorted(self.members, key=lambda m: m.get_degree()) == sorted(other.members, key=lambda m: m.get_degree())

    def differentiate(self):
        result = TPoly()
        for member in self.members:
            differentiated_member = member.differentiate()
            if differentiated_member.get_coeff() != 0:
                result.members.append(differentiated_member)
        return result

    def evaluate(self, x):
        value = 0
        for member in self.members:
            value += member.evaluate(x)
        return value

    def element(self, i):
        try:
            return self.members[i].get_coeff(), self.members[i].get_degree()
        except IndexError:
            raise IndexError("Index out of bounds")

    def __repr__(self):
        return f"TPoly({self.members})"