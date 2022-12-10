fun main() {
    fun calcPriority(char: Char) : Int{
        return if (char.isUpperCase()){
            char.code - 38
        } else {
            char.code - 96
        }
    }

    fun part1(input: List<String>): Int {
        var soma = 0
        input.forEach {
            val len = it.length
            val pocket1 = it.substring(0, len/2)
            val pocket2 = it.substring(len/2, len)
            val char = pocket1.first { char -> char in pocket2 }
            val priority = if (char.isUpperCase()){
                char.code - 38
            } else {
                char.code - 96
            }
            soma += priority
        }
        return soma
    }

    fun part2(input: List<String>): Int {
        var soma = 0
        for (i in 0 until input.size-1 step 3) {
            val badge = input[i].first { char -> char in input[i+1] && char in input[i+2]}
            soma+=calcPriority(badge)
        }

        return soma
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day03_test")
    check(part1(testInput) == 157)
    check(part2(testInput) == 70)

    val input = readInput("Day03")
    println("Part 1:")
    println(part1(input))
    println("Part 2:")
    println(part2(input))
}
