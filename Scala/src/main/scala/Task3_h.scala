object Task3_h {
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
    var new_sal_dep: List[Int] = List()
    for (n <- res){
      new_sal_dep = new_sal_dep :+ (n*1.07).toInt
      }
    println(new_sal_dep)
    }

}
