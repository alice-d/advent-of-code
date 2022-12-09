import java.lang.RuntimeException

enum class RPS(val score: Int) {
    ROCK(1), PAPER(2), SCISSORS(3)
}
enum class RESULT(val score: Int) {
    WIN(6), TIE(3), LOSE(0)
}

val abc = mapOf(
    "A" to RPS.ROCK,
    "B" to RPS.PAPER,
    "C" to RPS.SCISSORS
)

fun play(mine: RPS, other: RPS) : RESULT{
    if (mine == other)
        return RESULT.TIE

    return when (mine){
        RPS.ROCK -> when (other){
            RPS.PAPER -> RESULT.LOSE
            RPS.SCISSORS -> RESULT.WIN
            else -> throw RuntimeException("")
        }
        RPS.PAPER -> when (other) {
            RPS.ROCK -> RESULT.WIN
            RPS.SCISSORS -> RESULT.LOSE
            else -> throw RuntimeException("")
        }
        RPS.SCISSORS -> when (other) {
            RPS.ROCK -> RESULT.LOSE
            RPS.PAPER -> RESULT.WIN
            else -> throw RuntimeException("")
        }
    }
}

fun playToResult(otherMove : RPS, result : RESULT) : RPS {
    return when (result){
        RESULT.TIE -> return otherMove
        RESULT.WIN -> when (otherMove) {
            RPS.ROCK -> RPS.PAPER
            RPS.PAPER -> RPS.SCISSORS
            RPS.SCISSORS -> RPS.ROCK
        }
        RESULT.LOSE -> when (otherMove) {
            RPS.ROCK -> RPS.SCISSORS
            RPS.PAPER -> RPS.ROCK
            RPS.SCISSORS -> RPS.PAPER
        }

    }
}

fun main() {
    fun part1(input: List<String>): Int {
        val xyz = mapOf(
            "X" to RPS.ROCK,
            "Y" to RPS.PAPER,
            "Z" to RPS.SCISSORS
        )

        var totalScore=0
        input.forEach {
            val game = it.split(" ")
            var myMove = xyz[game[1]]!!
            val adversaryMove =abc[game[0]]!!
            var score = myMove.score
            val result = play(myMove, adversaryMove)
            score += result.score
            totalScore+=score

        }
        //println(totalScore)
        return totalScore
    }

    fun part2(input: List<String>): Int {
        val xyz = mapOf(
            "X" to RESULT.LOSE,
            "Y" to RESULT.TIE,
            "Z" to RESULT.WIN
        )
        var totalScore=0
        input.forEach {
            val game = it.split(" ")
            var resultIWant = xyz[game[1]]!!
            val adversaryMove =abc[game[0]]!!
            var score = resultIWant.score
            val myMove = playToResult(adversaryMove, resultIWant)
            score += myMove.score
            totalScore+=score

        }
        //println(totalScore)
        return totalScore
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day02_test")
    check(part1(testInput) == 15)
    check(part2(testInput) == 12)

    val input = readInput("Day02")
    println("Part 1:")
    println(part1(input))
    println("Part 2:")
    println(part2(input))
}
