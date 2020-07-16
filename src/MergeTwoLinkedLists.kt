import common.ListNode

/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 *
 * Example: 1 -> 2 -> 4, 1 -> 3 -> 4
 * Result: 1-> 1 -> 2 -> 3 -> 4 -> 4
 */
fun main() {
    val nodeA1 = ListNode(1)
    val nodeA2 = ListNode(2)
    val nodeA4 = ListNode(4)

    val nodeB1 = ListNode(1)
    val nodeB3 = ListNode(3)
    val nodeB4 = ListNode(4)

    nodeA1.next = nodeA2
    nodeA2.next = nodeA4

    nodeB1.next = nodeB3
    nodeB3.next = nodeB4

    val m: MergeTwoLinkedLists = MergeTwoLinkedLists()
    var head = m.mergeTwoLists(nodeA1, nodeB1)
    while (head != null) {
        println(head.value)
        head = head.next
    }
}

class MergeTwoLinkedLists {
    fun mergeTwoLists(l1: ListNode?, l2: ListNode?): ListNode? {
        var head: ListNode? = null
        var pointer1 = l1
        var pointer2 = l2
        // 1->3->4, 2
        var before: ListNode? = null
        while (pointer1 != null || pointer2 != null) {

            if (pointer1 != null && pointer2 == null) {
                // List 2 no elements anymore
                if (before != null) {
                    before.next = pointer1
                } else {
                    head = pointer1
                }
                before = pointer1
            } else if (pointer1 == null && pointer2 != null) {
                // List 1 no elements anymore
                if (before != null) {
                    before.next = pointer2
                } else {
                    head = pointer2
                }
                before = pointer2
                pointer2 = pointer2.next
            } else if (pointer1 != null && pointer2 != null) {
                // Compare pointers of both lists
                var smallerPointer: ListNode?
                if (pointer1.value <= pointer2.value) {
                    smallerPointer = pointer1
                    pointer1 = pointer1.next
                } else {
                    smallerPointer = pointer2
                    pointer2 = pointer2.next
                }
                if (before != null) {
                    before.next = smallerPointer
                } else {
                    head = smallerPointer
                }
                before = smallerPointer
            }
        }
        return head
    }
}

