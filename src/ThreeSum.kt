fun main(args: Array<String>) {
    val s: Solution = Solution()
    val list: List<List<Int>> = s.threeSum(intArrayOf(-1, 0, 1, 2, -1, -4))
    println(list.size)
    list.forEach { triplet -> println(triplet.joinToString(separator = ", ", prefix = "[", postfix = "]")) }
}

class Solution {

    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        var answer: Set<List<Int>> = mutableSetOf()
//        var answer: List<List<Int>> = mutableListOf()

        for (ax in nums.indices) {
            for (bx in ax + 1 until nums.size) {
                for (cx in bx + 1 until nums.size) {
                    val a = nums[ax]
                    val b = nums[bx]
                    val c = nums[cx]

                    if (a + b + c == 0) {
                        answer = answer.plusElement(listOf(a, b, c))
                    }
                }
            }
        }

        return answer
            .map { entry -> entry.toList() }
    }
}