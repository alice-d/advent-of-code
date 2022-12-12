import java.util.Stack

fun main() {

    fun processStartBoxes(line : String, stacks: MutableList<ArrayDeque<Char>>){
        if (line.contains("1")) {
            return
        }

        var j=0
        for (i in 1..line.length step 4){
            val crate = line[i]
            if (crate != ' '){
                stacks[j].add(crate)
            }
            j+=1
        }
    }

    fun processMove(line: String, stacks: MutableList<ArrayDeque<Char>>){
        val numbers = Regex("[0-9]+").findAll(line)
            .map(MatchResult::value)
            .map {  it.toInt()}
            .toList()
        val quantity = numbers[0]
        val from = numbers[1]-1
        val to = numbers[2]-1

        for (i in 1..quantity){
            val removed = stacks[from].removeFirst()
            stacks[to].addFirst(removed)
        }

    }

    fun part1(input: List<String>): String {
        var stacks = mutableListOf(ArrayDeque<Char>())
        for (i in 1..10){
            stacks.add(ArrayDeque())
        }

        var movementsProcessing = false

        input.forEach {
            if (movementsProcessing) processMove(it, stacks)
            else if (it=="") movementsProcessing = true
            else processStartBoxes(it, stacks)
        }

        var result = ""
        for (stack in stacks){
            if (stack.size>0)
                result+=stack.first()
        }

        return result
    }

    fun processMove2(line: String, stacks: MutableList<ArrayDeque<Char>>){
        val numbers = Regex("[0-9]+").findAll(line)
            .map(MatchResult::value)
            .map {  it.toInt()}
            .toList()
        val quantity = numbers[0]
        val from = numbers[1]-1
        val to = numbers[2]-1

        val removed = ArrayDeque<Char>()
        for (i in 1..quantity){
            removed.addFirst(stacks[from].removeFirst())
        }
        removed.forEach{
            stacks[to].addFirst(it)
        }
    }

    fun part2(input: List<String>): String {
        var stacks = mutableListOf(ArrayDeque<Char>())
        for (i in 1..10){
            stacks.add(ArrayDeque())
        }

        var movementsProcessing = false

        input.forEach {
            if (movementsProcessing) processMove2(it, stacks)
            else if (it=="") movementsProcessing = true
            else processStartBoxes(it, stacks)
        }

        var result = ""
        for (stack in stacks){
            if (stack.size>0)
                result+=stack.first()
        }

        return result
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day05_test")
    check(part1(testInput) == "CMZ")
    check(part2(testInput) == "MCD")

    val input = readInput("Day05")
    println("Part 1:")
    println(part1(input))
    println("Part 2:")
    println(part2(input))
}
