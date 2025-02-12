import csv 

def rec_instances(instance_type,cpu):
    i_sizes=["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]
    i_fam , size=instance_type.split(".")
    if size not in i_sizes:
        return "invalid"
    curr=i_sizes.index(size)
    if cpu<20 and curr>0:
        status="underutilized"
        rec=i_sizes[curr-1]
    elif cpu>80 and curr <len(i_sizes)-1:
        status="overutilized"
        rec=i_sizes[curr+1]
    else:
        status="optimized"
        rec=i_sizes[curr]
    rec_fam=i_fam.replace("t2","t3") if i_fam.startswith("t2") else i_fam
    rec_i=f"{rec_fam}.{rec}"
    return status,rec_i

def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    border = "+-" + "-+-".join("-" * width for width in col_widths) + "-+"
    
    print(border)
    for i, row in enumerate(data):
        print("| " + " | ".join(f"{item:{col_widths[j]}}" for j, item in enumerate(row)) + " |")
        print(border if i == 0 else border)  # Print border after the header and at the end
ec2_instance="t2.large"
cpu=20
status, rec_i=rec_instances(ec2_instance,cpu)
data = [["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"],
        ["1", ec2_instance, f"{cpu}%", status, rec_i]]

print_table(data)

