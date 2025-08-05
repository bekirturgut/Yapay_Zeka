from pomegranate import *

yagmur = Node(DiscreteDistribution({
    "yok": 0.7,
    "hafif": 0.2,
    "guclu": 0.1
}), name="yagmur")

bakım = Node(ConditionalProbabilityTable([
    ["yok","evet"]: 0.4,
    ["yok","hayir"]: 0.6,
    ["hafif","evet"]: 0.2,
    ["hafif","hayir"]: 0.8,
    ["guclu","evet"]: 0.1,
    ["guclu","hayir"]: 0.9
], [yagmur.distribution]), name="bakim")

