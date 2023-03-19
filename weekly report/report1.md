
# QG训练营人工智能组第一周周记：
2023年3月19日
---
--- 

<font color=#00ffff size=72>生活随记</font>
---

平淡的一周，除了QG训练营开营和新生杯外，其他照旧
---

---
<font color=#0099ff size=7 face="黑体">一周总结</font>
---
### 这周在计算机科学上，学到了链表的概念与其应用，并且在完成大组作业的过程中，发现了许多细节问题。
---
### 在基础学科上，电路学习和大物让人犯难。
---
### 总结为需要分配好时间，时间有点紧迫，无论是训练营还是基础学科上
---

<font size="10"><font color="#dd0000">存在问题</font><br /></font><br />
---
### <font size="6"><font color="#00dd00">1.传值和传址问题</font><br /> </font><br /> 
#### <font size="4">常量其传值还是传址，很容易区分，对我影响不大。然而涉及到指针的指针这就让人有点头疼，其不仅容易造成野指针的出现，还很让人混乱.比如这次，我就给NULL->next报错了好几次</font><br />
---
### <font size="6"><font color="#0000dd">2.if语句中=和==</font><br /></font><br />
#### <font size="4">这个可以说是老毛病了，老是少加个等于号，完成链表的时候，好几次没加，整的不是死循环，就是无论输入什么都是一个结果。
---
### <font size="6"><font color="#dd00dd">3.让人难受的反转语句</font><br /></font><br />  
#### <font size="4">单链表反转就这一个函数实实在在整了我一个晚上还没整出。其中
LinkedList ReverseList(LNode* P)

{

    LinkedList firstnode=NULL;
    LinkedList p1=p;
    LinkedList p2=p1->next;
    while(p2!=NULL)
    {
        p1->next=firstnode;
        firstnode=p1;
        p1=p2;
        p2=p2->next;
    }
    p=p1;
    return p;

}

逻辑好像没什么问题，但输出时总是少了数据，之后上网看了别人的想法才写出来。。。
</font><br />
---
### <font size="6"><font color="#dddd00">4.最大问题，函数互相兼容问题</font><br /></font><br />
#### <font size="4">写完单链表后对链表熟悉了。在写双向链表花我四分之三的时间用在调试上。在写删除函数时，发现不管链表有多少个数据，监视之后发现，删除的数据其前面的数据全没了，其后面还在。所以我怀疑是不是初始化的问题，因为多了个指向前面，可能漏了，后面发现没问题。
调试几遍后，想到next都有，但front没有是不是add函数的原因，一看，果然是添加的数据其指向front没用前面数据的地址赋值；而我在写单链表，发现数据反转后，再用别的调用其他功能时发现，数据顺序变了。
</font><br />
### <font color="#dddd00"><font size="6">5.逻辑思维能力不够强，仍需锻炼</font><br /> 
</font><br /> 
---

## <font size="8"><font color="#006666">下周规划</font><br /></font><br />

<font size="4">初识和入门python
</font><br />

