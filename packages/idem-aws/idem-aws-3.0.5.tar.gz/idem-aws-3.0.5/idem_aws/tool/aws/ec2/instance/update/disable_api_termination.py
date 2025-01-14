from typing import List


async def apply(
    hub, ctx, resource, *, old_value, new_value, comments: List[str]
) -> bool:
    """
    Modify an ec2 instance based on a single parameter in it's "present" state

    Args:
        hub:
        ctx: The ctx from a state module call
        resource: An ec2 instance resource object
        old_value: The previous value from the attributes of an existing instance
        new_value: The desired value from the ec2 instance present state parameters
        comments: A running list of comments abound the update process
    """
    if new_value is None:
        ret = await hub.exec.boto3.client.ec2.reset_instance_attribute(
            ctx, InstanceId=resource.id, Attribute="disableApiTermination"
        )
        if ret.comment:
            comments.append(ret.comment)
        return ret.result
    else:
        ret = await hub.exec.boto3.client.ec2.modify_instance_attribute(
            ctx,
            InstanceId=resource.id,
            # Attribute="disableApiTermination",
            DisableApiTermination={"Value": new_value},
        )
        if ret.comment:
            comments.append(ret.comment)
        return ret.result
