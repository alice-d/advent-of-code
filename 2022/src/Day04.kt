fun main() {
    fun processRange(s: String): IntRange {
        val rangeNums = s.split("-")
        return rangeNums[0].toInt()..rangeNums[1].toInt()
    }

    fun part1(input: List<String>): Int {
        var sum = 0
        input.forEach {
            val pair = it.split(",")
            val range1 = processRange(pair[0])
            val range2 = processRange(pair[1])

            if (range1.all { num -> range2.contains(num) } || range2.all { num -> range1.contains(num) })
                sum += 1
        }
        return sum
    }

    fun part2(input: List<String>): Int {
        var sum = 0
        input.forEach { it ->
            //println(it)
            val pair = it.split(",")
            val range1 = processRange(pair[0])
            val range2 = processRange(pair[1])

            if (range1.any { num -> range2.contains(num) } || range2.any { num -> range1.contains(num) })
                sum += 1

        }
        return sum
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day04_test")
    check(part1(testInput) == 2)
    check(part2(testInput) == 4)

    val input = readInput("Day04")
    println("Part 1:")
    println(part1(input))
    println("Part 2:")
    println(part2(input))
}
