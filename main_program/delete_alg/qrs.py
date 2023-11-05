from main_program.Time import Time
from start_module.Variables import QRSdelete


class DeleteByQRS:
    def __init__(self, peak_x, start, finish, autoDelGr):
        self.peak_x = peak_x
        self.start = start
        self.finish = finish
        self.autoDel = autoDelGr

    def find_chains(self, seq):
        self.start
        chains = []
        current_chain = []

        for i in range(len(seq) - 1):
            if seq[i + 1] - seq[i] < QRSdelete.delta_time.getSeconds():
                if not current_chain:
                    current_chain.append(self.autoDel.find_nearest_data(seq[i])[0])
                current_chain.append(self.autoDel.find_nearest_data(seq[i+1])[1])
            else:
                if len(current_chain) > 5:  # Умова кількості елементів
                    chains.append([Time.getSecToTime(current_chain[0]),
                                   Time.getSecToTime(current_chain[-1])])  # Додати початок і кінець ланцюжка
                current_chain = []

        # Перевірка останнього елемента

        if len(current_chain) > QRSdelete.points_amount:
            chains.append([Time.getSecToTime(current_chain[0]), Time.getSecToTime(current_chain[-1])])

        return chains

    #
    def find_inverse_intervals(self, sequence=None):
        if sequence is None:
            sequence = self.find_chains(self.peak_x)
        inverse_intervals = []

        st = self.start
        for in_s in sequence:
            inverse_intervals.append([st, in_s[0]])
            st = in_s[1]
        inverse_intervals.append([st, self.finish])

        return inverse_intervals


if __name__ == "__main__":
    sequence = [16200.12, 16201.08, 16203.96, 16211.6, 16212.52, 16213.44, 16214.36, 16215.32, 16216.24, 16220.84,
                16222.8, 16223.32, 16224.52, 16229.88, 16230.44, 16231.12, 16231.72, 16232.92, 16233.44, 16234.04,
                16236.36, 16237.28, 16238.2, 16239.64, 16240.24, 16240.8, 16241.64, 16242.16, 16243.28, 16244.2,
                16246.8, 16251.64, 16252.32, 16252.92, 16254.68, 16258.32, 16259.28, 16264.48, 16265.92, 16267.08,
                16270.64, 16271.16, 16272.32, 16273.52, 16274.76, 16275.32, 16278.24, 16279.16, 16282.72, 16283.64,
                16284.16, 16286.56, 16288.92, 16290.64, 16292.6, 16294.2, 16295.48, 16296.48, 16299.12, 16301.76,
                16303.0, 16303.52, 16307.12, 16308.08, 16308.6, 16309.92, 16313.28, 16315.56, 16316.72, 16317.84,
                16321.76, 16325.28, 16325.84, 16327.16, 16328.24, 16328.8, 16329.36, 16331.8, 16332.36, 16332.92,
                16335.36, 16339.88, 16340.92, 16344.44, 16345.6, 16348.4, 16349.32, 16351.12, 16352.04, 16354.8,
                16356.72, 16357.68, 16358.64, 16359.6, 16362.4, 16369.08, 16370.04, 16371.0, 16371.96, 16372.92]

    dbqrs = DeleteByQRS(sequence, Time(4, 30, 0, 0), Time(5, 0, 0, 0))

    sequences = dbqrs.find_chains(sequence)
    s = dbqrs.find_inverse_intervals(sequences)
    for i in s:
        print("[", i[0], ",", i[1], "]")

    print("aaaaaaaaaaaaaaaa")
    for i in sequences:
        print("[", i[0], ",", i[1], "]")
