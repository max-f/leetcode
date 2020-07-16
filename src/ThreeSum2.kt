import java.io.File

fun main() {
    val s = ThreeSumSolution()
    val inputStrRaw = File("/home/keks/input_long").readText(Charsets.UTF_8)
    val inputStr = inputStrRaw.slice(1 until inputStrRaw.length - 1)
    val inputIntArr = inputStr.trim().split(",").toList().map { it.toInt() }.toIntArray()
//    Thread.sleep(2000)
//    val listOfResults = s.threeSum(inputIntArr)
    val listOfResults = measureTimeMillis({ time -> println("Duration: $time ms") }) { s.threeSum(inputIntArr) }
//    val listOfResults: List<List<Int>> = s.threeSum(intArrayOf(-1, 0, 1, 2, -1, -4))
//    val listOfResults: List<List<Int>> = s.threeSum(intArrayOf(0, 0, 0, 1, 1, -2, -2, 1, 1))
//    val listOfResults: List<List<Int>> = s.threeSum(intArrayOf(-1, -1, 2))
    println(listOfResults.size)
    listOfResults.forEach { triplet -> println(triplet.joinToString(separator = ", ", prefix = "[", postfix = "]")) }
//    s.twoSum(listOf(1, 2), 0)
}

inline fun <T> measureTimeMillisHere(
    loggingFunction: (Long) -> Unit,
    function: () -> T
): T {

    val startTime = System.currentTimeMillis()
    val result: T = function.invoke()
    loggingFunction.invoke(System.currentTimeMillis() - startTime)

    return result
}

class ThreeSumSolution {

    private var alreadySeen: MutableSet<Set<Int>> = mutableSetOf()

    fun threeSum(nums: IntArray): List<List<Int>> {

        val result = mutableListOf<List<Int>>()
        val allTwoSums = twoSum(nums.toList())

        for ( a in nums) {
            val complementingPairs = allTwoSums[-a] ?: continue
            for (pairSet in complementingPairs) {
                val b: Int = pairSet[0]
                val c: Int = pairSet[1]

                val tripletSet: Set<Int> = setOf(a, b, c)

                if (!alreadySeen.contains(tripletSet)) {
                    alreadySeen.add(tripletSet)
                    result.add(listOf(a, b, c))
                }
            }
        }
        return result
    }

    /**
     * Return all possible twoSums
     */
    private fun twoSum(nums: List<Int>): Map<Int, List<List<Int>>> {
        val allTwoSums: MutableMap<Int, MutableList<List<Int>>> = mutableMapOf()

        for ((ax, a) in nums.withIndex()) {
            for ((bx, b) in nums.withIndex()) {
                if (ax == bx) {
                    continue
                }

                val twoSum = a + b
                val tuple = listOf(a, b)
                val listToAdd = allTwoSums.getOrDefault(twoSum, mutableListOf())
                listToAdd.add(tuple)
                allTwoSums[twoSum] = listToAdd
            }
        }
        return allTwoSums
    }

}
