fun main() {
    fun countCalories(calories: List<String>) : MutableList<Int> {
        var currCalls=0
        val callsByElf = mutableListOf<Int>()
        calories.forEach {
            if(it.isEmpty()){
                callsByElf.add(currCalls)
                currCalls=0
                return@forEach
            }
            currCalls += it.toInt()
        }
        callsByElf.add(currCalls)
        return callsByElf
    }
    fun part1(calories: List<String>): Int {
        val callsByElf = countCalories(calories)
        return callsByElf.max()
    }

    fun part2(input: List<String>): Int {
        val callsByElf = countCalories(input)
        callsByElf.sortDescending()
        return callsByElf[0] + callsByElf[1] + callsByElf[2]
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day01_test")
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = readInput("Day01")
    println("Part 1:")
    println(part1(input))
    println("Part 2:")
    println(part2(input))
}
