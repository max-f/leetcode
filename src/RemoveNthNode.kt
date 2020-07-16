import common.ListNode

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
fun main() {
    var node1 = ListNode(1)
    var node2 = ListNode(2)
    var node3 = ListNode(3)
//    var node4 = ListNode(4)
//    var node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
//    node3.next = node4
//    node4.next = node5

    val r = RemoveNthNode()
    var head = r.removeNthFromEnd(node1, 1)
    while (head != null) {
        println(head.value)
        head = head.next
    }
}

class RemoveNthNode {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        val linkedListAsArrayList: MutableList<ListNode?> = mutableListOf()

        var tmpHead: ListNode? = head
        while (tmpHead != null) {
            linkedListAsArrayList.add(tmpHead)
            tmpHead = tmpHead.next
        }

        var before: ListNode? = null
        var after: ListNode? = null
        val idx: Int = linkedListAsArrayList.size - n
        if (idx > 0) {
            before = linkedListAsArrayList[idx - 1]
        }
        if (idx < linkedListAsArrayList.size - 1) {
            after = linkedListAsArrayList[idx + 1]
        }
        before?.next = after
        linkedListAsArrayList.removeAt(idx)
        if (linkedListAsArrayList.isNotEmpty()) {
            return linkedListAsArrayList[0]
        }
        return null
    }
}

