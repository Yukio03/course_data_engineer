import scala.io.StdIn.readInt

object Task3_c {
  def main(args: Array[String]) : Unit = {
    println("Введите годовой доход")
    val money = scala.io.StdIn.readInt()
    println("Введите размер премии в процентах")
    val pr: Double = scala.io.StdIn.readInt()
    println("Компенсация питания")
    val food = scala.io.StdIn.readInt()
    val sal_mon = money / 12
    val prem = (money * (pr/100)) / 12 /* премия в месяц */
    val salary: Double = sal_mon + prem + food /* оклад сотрудника в месяц */
    val sal_dep = Array(100, 150, 200, 80, 120, 75)
    val ave_sal: Double = sal_dep.sum / sal_dep.length /* средний оклад сотрудников */
    val dev_sal: Double = salary / ave_sal
    if (dev_sal >= 1) {
      println(((dev_sal * 100) - 100).round.toString + "%")
    }
     else {
      println(((dev_sal * 100) - 100).round.toString + "%")
    }
  }

}
