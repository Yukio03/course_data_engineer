object Task3_f {
  def main(args: Array[String]): Unit = {
    println("Введите годовой доход")
    val money = scala.io.StdIn.readInt()
    println("Введите размер премии в процентах")
    val pr: Double = scala.io.StdIn.readInt()
    println("Компенсация питания")
    val food = scala.io.StdIn.readInt()
    val sal_mon = money / 12
    val prem = (money * (pr / 100)) / 12
    /* премия в месяц */
    val salary = sal_mon + prem + food
    /* оклад сотрудника в месяц */
    val sal_dep = List(100, 150, 200, 80, 120, 75, 350, 90) :+ salary.toInt
    var res = sal_dep.sorted
    val new_sal = 130
    var ind_insert = 0
    for (n <- res.indices){
      if ((new_sal > res(n)) && (new_sal < res(n+1))){
        ind_insert = n+1
      }
    }
    def insert[T](list: List[T], i: Int, value: T) = {
      list.take(i) ++ List(value) ++ list.drop(i)
    }
    res = insert(res, ind_insert, new_sal)
    println(res)
  }
}
